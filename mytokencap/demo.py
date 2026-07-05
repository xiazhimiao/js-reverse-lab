import requests
import execjs

with open('1mytokencap_code生成逻辑.js', encoding='utf-8') as f:
    js_code = f.read()
    js = execjs.compile(js_code)
    code = js.call('get_params')

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "origin": "https://www.mytokencap.com",
    "priority": "u=1, i",
    "referer": "https://www.mytokencap.com/",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Microsoft Edge\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
}
url = "https://api.mytoken.info/ticker/currencyranklist"
params = {
    "pages": "1,1",
    "sizes": "100,100",
    "subject": "market_cap",
    "language": "en_US",
    "legal_currency": "USD",
    "code": code['code'],
    "timestamp": code['time'],
    "platform": "web_pc",
    "v": "0.1.0",
    "mytoken": ""
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
print(code)