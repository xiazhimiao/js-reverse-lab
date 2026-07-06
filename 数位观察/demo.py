import json
import execjs
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.swguancha.com",
    "Pragma": "no-cache",
    "Referer": "https://www.swguancha.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "deviceType": "1",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://app.swguancha.com/client/v1/article/client/page"
data = {
    "queryType": 3,
    "current": 1,
    "size": 20
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

with open('1数位观察.js', 'r') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
print(ctx.call('decrypt_data', response.text))
