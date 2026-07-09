import json
import requests
import subprocess

headers_info_str = subprocess.run(['node', '1.荔枝网.js'], capture_output=True, text=True, encoding='utf-8')
headers_info_dict = json.loads(headers_info_str.stdout)

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.gdtv.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.gdtv.cn/",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "x-itouchtv-ca-key": headers_info_dict['X-ITOUCHTV-Ca-Key'],
    "x-itouchtv-ca-signature": headers_info_dict['X-ITOUCHTV-Ca-Signature'],
    "x-itouchtv-ca-timestamp": str(headers_info_dict['X-ITOUCHTV-Ca-Timestamp']),
    "x-itouchtv-client": "WEB_PC",
    "x-itouchtv-device-id": headers_info_dict['X-ITOUCHTV-DEVICE-ID']
}
url = "https://gdtv-api.gdtv.cn/api/channel/v1/channel/2"
response = requests.get(url, headers=headers)

print(response.json())
