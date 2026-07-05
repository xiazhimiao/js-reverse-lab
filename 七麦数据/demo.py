import requests
import execjs
page = 10
with open('1七麦数据.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    run_js = execjs.compile(js_code)
    result = run_js.call('get_analysis', page)
    print(result)

# 基础配置
url = "https://api.qimai.cn/rank/release"
params = {
    "analysis": "ew8nHiYRSQ17SAcUKTVwQSgMPhw1PRlBfHMlAixTdxwoDlgPNwMFRnk3LRZ0XDwSKiwbDTdxZE0uHjgMbzIeFDFKTUd1EhgRBQ9SGRcDCw0ZCh91EgZRVlEJB1JSVVhOSDoWAg==",
    "genre": "36",
    "country": "cn",
    "date": "2026-07-01_2026-07-05",
    "is_preorder": "all",
    "status": "3",
    "sdate": "2026-07-01",
    "edate": "2026-07-05",
    "page": page
}

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Origin": "https://www.qimai.cn",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Microsoft Edge\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

cookies = {
    "qm_check": "A1sdRUIQChtxen8pI0dANi8zcX5zHBl+YnEhLyZIPxw8WkVRVRliYGBFVVdeSFk2VEdGX0kQc2gwRk9YAElKBQcABQsAHRghDxUNGw1JcQYDEE9Daw06VkcYCyZPagceEH0DcAlUT0VEWhoSUFRZEgMSBBRVSldESFVKF0o%3D",
    "PHPSESSID": "4s7j0ju16l49ajvtfqj1qul9i2",
    "gr_user_id": "f6dffed1-2d92-4721-bfaf-a643aefac74c",
    "aso_ucenter": "91cefnECvlw0w2wTpxiUdJGruwcxsZQq5VpPC91hImIkqtSUn%2BZLSZ5ItQEotTPoofo",
    "USERINFO": "6acMEhCKGRwg2ypyISEBSVukFJYP04hd3z689mpJon3Mamee56wwKJEJ41TOb0k0jGaxTVCn5OyLXGEoryeusZe03jOH%2BjH%2FW0Iyb50SHnXXpx4tzTrUA5vast3AKnQfF9Kl5gML9tCUqEsbLH35gA%3D%3D",
    "ada35577182650f1_gr_last_sent_cs1": "qm28321770430",
    "AUTHKEY": "xnZcIBR%2BqaWgMQ2j8IXAakCIkeY81Fquv6FiedkEyA2kTY5XYKtZ5k%2FEqHLsS9s6jgVQNf4MMPKr5s0cAyc%2BKUvpXRFHUgdp2zfwHS0IOjtxpleXHgVPwQ%3D%3D",
    "synct": "1783221270.704",
    "syncd": "-4032191",
    "ada35577182650f1_gr_session_id": "def1eb5e-d10f-4f13-af76-70da155d483d",
    "ada35577182650f1_gr_last_sent_sid_with_cs1": "def1eb5e-d10f-4f13-af76-70da155d483d",
    "ada35577182650f1_gr_cs1": "qm28321770430",
    "ada35577182650f1_gr_session_id_sent_vst": "def1eb5e-d10f-4f13-af76-70da155d483d"
}

# 发起请求
response = requests.get(url, headers=headers, cookies=cookies, params=params)

# 打印结果
print(f"状态码：{response.status_code}")
print(response.json())