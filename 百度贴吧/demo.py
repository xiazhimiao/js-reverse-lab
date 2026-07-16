"""
百度贴吧帖子列表爬虫 — 支持中文关键词搜索 & CSV 导出

tbs 说明：
  tbs 是百度贴吧的 CSRF 令牌（跨站请求伪造防护），由服务端通过
  /dc/common/tbs 接口下发，与客户端 Session（Cookie）绑定。
  即使未登录也能获取有效 tbs（is_login=0），但每个 POST 请求
  必须携带与当前 Session 匹配的 tbs，否则接口会返回签名校验失败。

  简言之：get tbs → 带着同一次会话的 cookie 去 POST → 成功。
  因此本脚本使用 requests.Session() 保持会话一致性。
"""

import csv
import json
import subprocess as _subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import execjs
import execjs._external_runtime as _ext_mod
import requests

# ── 修复 PyExecJS 在 Windows 上的 GBK/UTF-8 编码冲突 ────────
#    原代码 Popen(..., universal_newlines=True) 没带 encoding，
#    Windows 默认用 GBK 解码 Node 的 UTF-8 输出 → UnicodeDecodeError
_ext_mod.Popen = lambda *a, **kw: _subprocess.Popen(*a, encoding="utf-8", **kw)

# ── 确保 Windows 控制台能输出中文 ──────────────────────────
sys.stdout.reconfigure(encoding="utf-8")

# ── 路径 ──────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
JS_PATH = BASE_DIR / "Sign生成.js"
CSV_DIR = BASE_DIR / "csv"

# ── 签名：execjs 调用 JS 函数（无子进程，编译一次复用）────────
_JS_CTX = execjs.compile(
    JS_PATH.read_text(encoding="utf-8")
    .split("// 命令行:", 1)[0]  # 切掉 CLI 入口，只保留函数定义
)


def get_sign(data: dict, subapp_type: str = "pc") -> dict:
    """调用 JS get_sign 函数，返回带 sign 字段的完整字典。"""
    return _JS_CTX.call("get_sign", data, subapp_type)


# ── 翻页请求 ──────────────────────────────────────────────
def fetch_page(
    session: requests.Session,
    tbs: str,
    kw: str,
    pn: int,
    forum_id: str = "",
) -> dict:
    """
    请求一页帖子列表。

    kw 支持直接传入中文 — requests 会自动 URL 编码为
    application/x-www-form-urlencoded 格式，与 sign 的计算方式兼容。

    参考浏览器抓包 frs_page_pc_raw.py，补齐了 forum_id / tab_id / is_good
    等字段，确保分页与服务端行为一致。
    """
    data = {
        "kw": kw,
        "pn": str(pn),
        "is_good": "0",
        "cid": "",
        "sort_type": "3",
        "tab_id": "1",
        "tab_type": "13",
        "tab_name": "热门",
        "forum_id": forum_id,
        "is_newfrs": "1",
        "is_newfeed": "1",
        "rn": "30",
        "rn_need": "10",
        "tbs": tbs,
        "subapp_type": "pc",
        "_client_type": "20",
    }
    signed = get_sign(data)
    return session.post(
        "https://tieba.baidu.com/c/f/frs/page_pc",
        headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/150.0.0.0 Safari/537.36"
            ),
        },
        data=signed,
        timeout=15,
    ).json()


# ── 从 feed 中提取作者名 ───────────────────────────────────
def _extract_author(feed: dict) -> str:
    """从 components → feed_head → main_data 中取作者昵称。"""
    for comp in feed.get("components", []):
        if comp.get("component") == "feed_head":
            for item in comp.get("feed_head", {}).get("main_data", []):
                if item.get("type") == 1:
                    return item.get("text", {}).get("text", "")
    return ""


# ── 从 feed 中提取帖子链接 ─────────────────────────────────
def _extract_url(biz: dict) -> str:
    """根据 thread_id 拼接帖子链接。"""
    tid = biz.get("thread_id", "")
    return f"https://tieba.baidu.com/p/{tid}" if tid else ""


# ── 解析单条 feed ─────────────────────────────────────────
def parse_feed(item: dict) -> dict | None:
    """将原始 feed 解析为结构化字典，非 feed 类型返回 None。"""
    if item.get("layout") != "feed":
        return None

    feed = item.get("feed", {})
    biz = feed.get("business_info_map", {})

    create_ts = int(biz.get("create_time", 0))
    create_time = (
        datetime.fromtimestamp(create_ts).strftime("%Y-%m-%d %H:%M:%S")
        if create_ts else ""
    )

    return {
        "thread_id":   biz.get("thread_id", ""),
        "title":       biz.get("title", ""),
        "abstract":    biz.get("abstract", ""),
        "author":      _extract_author(feed),
        "forum_name":  biz.get("forum_name", ""),
        "view_num":    biz.get("view_num", ""),
        "create_time": create_time,
        "url":         _extract_url(biz),
    }


# ── 终端格式化输出 ─────────────────────────────────────────
def print_results(rows: list[dict], page: int):
    """在终端整齐地打印一页帖子。"""
    print(f"\n{'─' * 70}")
    print(f"  第 {page} 页  ·  共 {len(rows)} 条")
    print(f"{'─' * 70}")

    for i, r in enumerate(rows, 1):
        print(f"  [{i:02d}] {r['title']}")
        print(f"       作者: {r['author']}  ·  浏览: {r['view_num']}  ·  {r['create_time']}")
        if r["abstract"]:
            # 摘要截断到 100 字符
            ab = r["abstract"][:100]
            print(f"       摘要: {ab}")
        print()


# ── CSV 导出 ──────────────────────────────────────────────
def save_csv(all_rows: list[dict], kw: str):
    """将所有帖子保存到 csv 目录下的 CSV 文件。"""
    CSV_DIR.mkdir(exist_ok=True)
    filename = CSV_DIR / f"贴吧_{kw}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    fieldnames = [
        "thread_id", "title", "abstract", "author",
        "forum_name", "view_num", "create_time", "url",
    ]
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"\n  ✅ CSV 已保存至: {filename}")


# ═══════════════════════════════════════════════════════════
#  主流程
# ═══════════════════════════════════════════════════════════
def main():
    KW = "三角洲行动"          # ← 注意是"三角洲行动"，不是"三角行动"
    MAX_PAGES = 20              # 安全上限，实际由 has_more 控制

    session = requests.Session()

    # ① 获取 tbs —— 必须在 Session 内拿，保证 cookie 与后续请求一致
    tbs_resp = session.get("https://tieba.baidu.com/dc/common/tbs", timeout=10)
    tbs_resp_json = tbs_resp.json()
    tbs = tbs_resp_json["tbs"]
    print(f"  tbs = {tbs}  (is_login={tbs_resp_json.get('is_login')})")

    all_rows: list[dict] = []
    forum_id = ""  # 第一页响应中提取

    for pn in range(1, MAX_PAGES + 1):
        resp = fetch_page(session, tbs, KW, pn, forum_id)

        # 检查是否有错误
        if resp.get("error_code"):
            print(f"  ⚠ 第{pn}页出错: {resp.get('error_msg', '未知错误')} (code={resp['error_code']})")
            break

        # 首页提取 forum_id，后续翻页带上
        if pn == 1:
            forum = resp.get("forum", {})
            forum_id = str(forum.get("forum_id", forum.get("id", "")))
            forum_name = forum.get("forum_name", forum.get("name", ""))
            print(f"  吧名: {forum_name}  (forum_id={forum_id})")

        feed_list = resp.get("page_data", {}).get("feed_list", [])
        rows = [parsed for item in feed_list if (parsed := parse_feed(item))]
        all_rows.extend(rows)

        print_results(rows, pn)

        # ② 根据服务端分页信息判断是否还有下一页
        page_info = resp.get("page", {})
        has_more = page_info.get("has_more", 0)
        total_page = page_info.get("total_page", 0)
        if not has_more:
            print(f"  📄 已到最后一页 (total_page={total_page})")
            break

        time.sleep(1)

    # ③ 保存 CSV
    if all_rows:
        save_csv(all_rows, KW)
    else:
        print("  ⚠ 没有获取到任何帖子，跳过 CSV 保存。")


if __name__ == "__main__":
    main()
