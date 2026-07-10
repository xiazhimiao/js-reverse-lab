import re
import json
import requests
import subprocess

# 在解密数据时如果出现编码报错则使用偏函数修改process默认编码
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "app-guestid": "5B3A0A7CB71F06CB8E2AF8B9CBE88841",  # 多次请求会导致此参数失效, 建议修改成动态值
    "app-version": "0",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://hangzhou.qccqcc.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://hangzhou.qccqcc.com/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

url = 'https://hangzhou.qccqcc.com/'
response = requests.get(url, headers=headers).text
key = re.findall('var qccppm = "(.*?)";', response)[0]

api_url = "https://newopenapiweb.17qcc.com/api/services/app/SearchFactory/GetPageList"
with open('./杭州服装.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
result = ctx.call('encrypt_payload', key)
data = {
    "Content": result['Content'],
    "Sign": result['Sign'],
    "RsaPubAes": result['RsaPubAes'],
    "IV": result['IV'],
    "TimesTamp": result['TimesTamp']
}

data = json.dumps(data, separators=(',', ':'))
response = requests.post(api_url, headers=headers, data=data)
result = response.json()['Result']
decrypt_response = ctx.call('decrypt_response', key, result)
print(decrypt_response)
