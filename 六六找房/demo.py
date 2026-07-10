import execjs
import requests

with open('六六找房.js', 'r', encoding='utf-8') as file:
    js_code = file.read()

ctx = execjs.compile(js_code)
# print(ctx.call('encrypt_authorization'))

url = "https://66miniapp-api.66zhizu.com/client/search/house"
params = {
    # 请求序列标识符: 用于标识和跟踪请求的顺序关系, 在每次请求后会被更新为响应中的新值
    'sequence': '1760948760.771;1761048607.898',
    'city': '上海',
    'region': '',
    'distance': '',
    'longitude': '',
    'latitude': '',
    'stations': '',
    'bed_count': '',
    'rent_type': '',
    'sort': '',
    'cost1': '',
    'cost2': '',
}

for _ in range(10):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        # "Authorization": "timestamp=1752666656;oauth2=aa77433d7c375a6031b60651a48f1504;signature=be53fad9e29e63f7ed83d2400f157abf;secret=aa77433d7c375a6031b60651a48f1504",
        "Authorization": ctx.call('encrypt_authorization'),
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Referer": "https://servicewechat.com/wxa0545fcd02d93b5d/196/page-frame.html",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Terminal": "windows",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/8555",
        "xweb_xhr": "1"
    }
    response = requests.get(url, headers=headers, params=params).json()
    print(response['result']['sequence'])
    params['sequence'] = response['result']['sequence']
    headers['Authorization'] = ctx.call('encrypt_authorization')
    print(response)
