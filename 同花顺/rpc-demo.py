import requests

data = {
    "group": "ths_rpc",
    "action": "ths_get_cookie",
}
response = requests.get("http://127.0.0.1:5620/business-demo/invoke", params=data)
cookie = response.json().get('data')
print(cookie)

headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://q.10jqka.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "hexin-v": cookie,
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "v": cookie
}
url = "https://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
