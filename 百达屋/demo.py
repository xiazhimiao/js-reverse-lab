import json
import execjs
import requests

with open('百达屋.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
result = ctx.call('get_headers_info')

headers = {
    "authority": "api.betterwood.com",
    "businesstype": "1",
    "messageid": result['messageid'],
    "pagesize": "20",
    "pageno": "4",
    "apptype": "2",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1 wechatdevtools/1.06.2504010 MicroMessenger/8.0.5 Language/zh_CN webview/ sessionid/5",
    "content-type": "application/json",
    "appversion": "3.5.6",
    "osversion": "iOS 10.0.1",
    "devicemanufacture": "devtools",
    "signature": result['signature'],
    "channel": "bdw",
    "timestamp": str(result['timestamp']),
    "clienttype": "5",
    "devicemodel": "iPhone 12/13 (Pro)",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx51868eb0fe8a83e2/devtools/page-frame.html",
    "accept-language": "zh-CN,zh;q=0.9"
}
url = "https://api.betterwood.com/base/app/store/listV2"
data = {
    "querySource": 2,
    "channelType": 1,
    "sourceType": 10,
    "serviceType": [
        "3"
    ],
    "searchType": 0,
    "dateStartTime": 1752681600000,
    "dateEndTime": 1752768000000,
    "destination": "国内/国际"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)
print(response.json())
