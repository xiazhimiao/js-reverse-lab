import execjs
import requests

with open('邯郸公示 - payload.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx_payload = execjs.compile(js_code)

with open('邯郸公示 - response.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx_response = execjs.compile(js_code)

for page in range(1, 2):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "C-GATEWAY-QUERY-ENCRYPT": "1",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://credit.hd.gov.cn/xyxxgs/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "x-gateway-body": "blob"
    }
    cookies = {
        "_gscu_2016493642": "51638795qogpxm10",
        "_gscbrs_2016493642": "1",
        "_gscs_2016493642": "517997995j46wo10|pv:3"
    }
    url = "https://credit.hd.gov.cn/zx_website/website/sgs/xzcffr"
    response = requests.get(url, headers=headers, cookies=cookies,
                            params=ctx_payload.call('generateRequestPayload', page))

    result = ctx_response.call('decrypt_response', list(response.content))
    print(result)
