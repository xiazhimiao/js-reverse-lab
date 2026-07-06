import execjs
import requests
from jsonpath import jsonpath

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "text/xml;charset=UTF-8",
    "Origin": "https://www.ccprec.com",
    "Pragma": "no-cache",
    "Referer": "https://www.ccprec.com/projectSecPage/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
url = "https://www.ccprec.com/honsanCloudAct"

with open('1吉林长春产权交易中心.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

for page in range(1, 7):
    payload = ctx.call('get_payload', {
        "id": "rtvg4qbdhioxgp8x",
        "projectKey": "honsan_cloud_ccprec",
        "clientKey": "rtvg3h42e00xrl6i",
        "token": None,
        "clientDailyData": {},
        "acts": [{
            "id": "rtvg4q5kidcsdbx2",
            "fullPath": "/ccprec.com.cn.web/client/info/cqweb_nonphy_cqzr",
            "args": [page, 20, None]
        }]
    })

    response = requests.post(url, headers=headers, data=payload)
    result = ctx.call('get_data', response.text)
    create_date = jsonpath(result, '$..create_date')
    object_name = jsonpath(result, '$..object_name')

    for item in zip(object_name, create_date):
        item = {
            "object_name": item[0],
            "create_date": item[1]
        }
        print(item)
