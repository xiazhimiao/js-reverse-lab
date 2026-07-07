import execjs
import requests

with open('医保局请求头参数加密.js', encoding='utf-8') as f:
    js_code = f.read()
js = execjs.compile(js_code)
result = js.call('get_headers', 1)

headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fuwu.nhsa.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-Tingyun": "c=B|4Nl_NnGbjwY;x=eb4590a5c218452a",
    "channel": "web",
    "contentType": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "x-tif-nonce": result['headers']['x-tif-nonce'],
    "x-tif-paasid": "undefined",
    "x-tif-signature": result['headers']['x-tif-signature'],
    "x-tif-timestamp": str(result['headers']['x-tif-timestamp'])
}
cookies = {
    "amap_local": "430100",
    "acw_tc": "1a0c639017514591475936710e006317e2a0463607c2433d6ff29650e1f9e7"
}
url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"

data = result['data']
response = requests.post(url, headers=headers, cookies=cookies, data=data)

with open('医保局响应体解密.js', encoding='utf-8') as f:
    js_code = f.read()

js = execjs.compile(js_code)
result = js.call('decrypt_data', response.json())
print(result)
