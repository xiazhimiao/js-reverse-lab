# 下一次请求携带的cookie是上一次请求的set-cookie信息, 则使用session请求完成

import json
import requests
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Auth-Plus;": "",
    "Client-Encrypt": "v1.1",
    "Connection": "keep-alive",
    "Origin": "https://www.hanghangcha.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "clientInfo": "web",
    "clientVersion": "1.0.7",
    "currentHref": "https://www.hanghangcha.com/hhcreport",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Microsoft Edge\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "Hm_lvt_1521e0fb49013136e79181f2888214a7": "1783393100",
    "Hm_lpvt_1521e0fb49013136e79181f2888214a7": "1783393100",
    "HMACCOUNT": "F62661461FEEA3F0",
    "JSESSIONID": "9F5CEAB41B5732F3C55FA913EDDE5609",
    "WX_OPEN": "ejduKNgPvTSQjAMdGZyMKQpbBXfLh4NgwUh/wf260MNnwbimehd4sSplb0Dr1Ako5qTWEvTLdu0Xq0EPUmg5RzxBcIbPN5WTSJh6OOk63TQ4GKeOI4+OdpY4RhY9bMie",
    "_ACCOUNT_": "ZTc2YmU5NzRmNmEyNGUyMTkyODliODMyNWFiYzBmMDYlNDAlNDBtb2JpbGU6MTc4NDYwMjcyNDc2NjoxYjI0NDY3YTJjNGFmNmE3NWRlYzFiN2Y0MzE1MTg2OQ"
}

session = requests.session()
for page in range(0, 6):
    params = {
        'filter': '{"reportType":null,"limit":10,"skip":%d}' % (page * 10),
    }

    if page == 0:
        response = session.get(
            'https://api.hanghangcha.com/hhc/member/industry/getReportList',
            params=params,
            cookies=cookies,
            headers=headers,
        )
    else:
        response = session.get(
            'https://api.hanghangcha.com/hhc/member/industry/getReportList',
            params=params,
            headers=headers,
        )

    enc_data = response.json().get('data')
    with open('行行查.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    result = ctx.call('decrypt', enc_data)
    print(json.loads(result))
