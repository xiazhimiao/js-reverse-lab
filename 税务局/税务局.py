import requests
import subprocess
# 解决execjs乱码
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
from lxml import etree

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://etax.ningbo.chinatax.gov.cn:8443/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

# 补上你原来的cookies字典（缺失导致NameError）
cookies = {
    "ZDO0ZhZUfw4xO": "60VP62sxCC3UAap7oy8rs2nNV1sHVXuMgZFzOvxtralTqdG8FBa.vnFUeQMNB7gcUEXCdzge8NPESa.haZ0nlrIa",
    "ZDO0ZhZUfw4xP": "0el6Gy8bM_FQVqBas8wuSccJ7BjFYKa1VnUHyVBx9.8MDcz96AFp2wbPjoXTAsqB_ZASxZ_IKcEetZWwnN4dpOVSnNPr2B3C0d8tTnKeDhKWEwd0QRzvgOE5AQaRVaKtB2XFpDAo9QUd2W2AsOQ0Vd8EcbV_71z4tFipJ92179635SnWC47yH0xihE0f32Q0lIwEkYhi2XQY6B9wR00jyh1lnbc.HTKiv0O6m5iXcAEGjLOSBL.PdcCXTPfZCf7wmgZCjl3ZzVR_JqgBarIVZZnaQwX68M.EvUdK2tkSibjgVeZgB8JfXxn0zwMBYR0IZjy6W7kxUtNl862tQJ6AJqRwZYZH811p.CCVl64oHhVrujddAmb4PDEmgIxL3M0u4KZWiTZsY617QGpmtOuxd8gEEuuFoyMscC5fd7cRmVEo7MRz5zBKhzN6ixC.8w.RDmN_9cbIPYsczblUN7jY5Sa"
}

# 目标站点，末尾不要斜杠
base_url = "https://etax.ningbo.chinatax.gov.cn:8443"
session = requests.session()
# 传入初始cookies
session.cookies.update(cookies)

# 1. 请求首页拿到加密页面HTML
resp = session.get(base_url, headers=headers, verify=False)
resp.encoding = "utf-8"
html_text = resp.text
tree = etree.HTML(html_text)

# 2. 提取meta标签content（对应你JS里的content变量）
meta_content = tree.xpath('//meta[@id="HRHkMu6mGL8x"]/@content')[0]
print("meta_content提取值：", meta_content)

# 3. 提取页面内联加密JS encrypt_js_code
encrypt_js_code = tree.xpath('//script[not(@src)]/text()')[0].strip()

# 4. 提取外部解密JS地址并请求拿到decrypt源码
decrypt_js_path = tree.xpath('//script[@src and position()=2]/@src')[0]
decrypt_js_full_url = base_url + decrypt_js_path
decrypt_js_code = session.get(decrypt_js_full_url, headers=headers, verify=False).text

# 5. 读取本地补环境JS，替换占位符
with open("mod.js", "r", encoding="utf-8") as f:
    js_env_code = f.read()
# 替换三个占位符，和案例逻辑对齐
js_env_code = js_env_code.replace('var content = "meta_content"', f'var content = "{meta_content}"')
js_env_code = js_env_code.replace("'encrypt_js_code'", encrypt_js_code)
js_env_code = js_env_code.replace("'decrypt_js_run_code'", decrypt_js_code)

# 6. 编译JS环境，执行获取cookie
ctx = execjs.compile(js_env_code)
cookie_str = ctx.call("get_cookie")
print("JS算出完整cookie字符串：", cookie_str)

# # 7. 更新session cookie，携带新cookie重新请求页面
# cookie_kv = {}
# for item in cookie_str.split(";"):
#     item = item.strip()
#     if not item:
#         continue
#     k, v = item.split("=", 1)
#     cookie_kv[k] = v
# session.cookies.update(cookie_kv)

# 7. 更新Session Cookie（修复版）
cookie_kv = {}
cookie_str = ctx.call("get_cookie")
# 只取 ; 分割后的第一段纯cookie键值，丢弃 path/expires/Secure 等多余参数
pure_cookie_part = cookie_str.split(";")[0].strip()
k, v = pure_cookie_part.split("=", 1)
cookie_kv[k] = v
session.cookies.update(cookie_kv)


# 携带生成后的新cookie访问目标页面
final_resp = session.get(base_url, headers=headers, verify=False)
# 强制utf-8编码，解决中文转义乱码
final_resp.encoding = "utf-8"
print("响应状态码：", final_resp.status_code)
print("页面源码：", final_resp.text)

# 可选：写入本地HTML文件，打开完全无乱码
# with open("解密页面.html", "w", encoding="utf-8") as f:
#     f.write(final_resp.text)
# print("页面已保存至 解密页面.html，本地打开中文正常")
