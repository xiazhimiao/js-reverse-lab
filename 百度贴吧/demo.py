import requests
import subprocess
import json
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

JS_PATH = r"/Sign生成.js"


def get_sign(data: dict) -> dict:
    result = subprocess.run(
        ["node", JS_PATH, json.dumps(data, ensure_ascii=False)],
        capture_output=True, text=True, encoding="utf-8",
    )
    return json.loads(result.stdout)


def fetch_page(tbs: str, kw: str, pn: int) -> dict:
    data = {
        "kw": kw, "pn": str(pn), "sort_type": "3",
        "is_newfrs": "1", "is_newfeed": "1", "rn": "30", "rn_need": "10",
        "tbs": tbs, "subapp_type": "pc", "_client_type": "20",
    }
    data = get_sign(data)
    return requests.post(
        "https://tieba.baidu.com/c/f/frs/page_pc",
        headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
        data=data, timeout=10,
    ).json()


# 拿 tbs
tbs = requests.get("https://tieba.baidu.com/dc/common/tbs", timeout=10).json()["tbs"]

# 翻两页
for pn in [1, 2]:
    resp = fetch_page(tbs, "python", pn)
    feed_list = resp.get("page_data", {}).get("feed_list", [])
    print(f"===== 第{pn}页 ({len(feed_list)}条) =====\n")

    for item in feed_list:
        if item.get("layout") != "feed":
            continue
        abstract = item.get("feed", {}).get("business_info_map", {}).get("abstract", "")
        print(f"  {abstract[:80]}\n")

    time.sleep(1)
