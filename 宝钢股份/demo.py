import json
import execjs
import requests

for page in range(10):
    print(f"第{page + 1}页:")
    run_js = execjs.compile(open("1宝钢股份.js", encoding="utf-8").read()).call("get_data", page)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Md5": run_js["Content-Md5"],
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://www.baosteel.com",
        "Pragma": "no-cache",
        "Referer": "https://www.baosteel.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "x-date": str(run_js["x-date"]),
        "x-nonce": run_js["x-nonce"],
        "x-signature": run_js["x-signature"],
        "x-user": "0/56f5cff3cad14853a44782c2c689ab2a"
    }
    url = "https://cmsauth.baowugroup.com/v1/web/api/content/list"
    params = {
        "domainId": "12"
    }
    data = {
        "pageNo": page,
        "pageSize": 12,
        "condition": {
            "nodeId": 436
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, params=params, data=data)

    for temp in response.json()['data']['data']:
        print(temp)
