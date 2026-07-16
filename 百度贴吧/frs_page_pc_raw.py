import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://tieba.baidu.com",
    "Referer": "https://tieba.baidu.com/f?kw=%E4%B8%89%E8%A7%92%E6%B4%B2%E8%A1%8C%E5%8A%A8&fr=frs",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Microsoft Edge\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-requested-with": "XMLHttpRequest",
}

cookies = {
    "BIDUPSID": "46327DA8AD1694B8DF8B5FD33C0D5130",
    "PSTM": "1782357387",
    "newlogin": "1",
    "BAIDUID": "363D6C4BD5CC9B832936EDAF9290412E:FG=1",
    "BAIDUID_BFESS": "363D6C4BD5CC9B832936EDAF9290412E:FG=1",
    "ZFY": "psZ3Q7L74Od7DFT6hmqNmpvWs0:BL2hRABdiaR9T68go:C",
    "RT": "\"z=1&dm=baidu.com&si=07eda957-b3b2-4afe-8008-8b966f28de6f&ss=mrg4vhwu&sl=1&tt=1aj&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2aa&ul=bsp&hd=bsy\"",
    "H_PS_PSSID": "63148_67862_68166_69295_71139_71268_71304_71316_71364_71358_71354_71366_71234_71429_71464_71477_71483_71415_71520_71550_71538_71534_71533_71541_71544_71562_71560_71553_71556_71566_71585_71588_71603_71622_71638_71643_71657_71504_71681_71685_71710_71765_71791_71725_71741_71812_71898_71915_71908",
    "USER_JUMP": "-1",
    "BAIDU_WISE_UID": "wapp_1784193412043_152",
    "__bid_n": "19f6a374dc843688e6d8f3",
    "ab_sr": "1.0.1_MGVmYTE1YjY5MjAxOWQxZTg2ZjAwMmE0Y2QzMjI2MjdiYjU4MjlkMWY3MjM5ZDc4Y2JiY2NkZjE2NTUwNTQ2OTNlNjc5MTM0NzhmNmQ2YWRjZWI1ZjQzZmE0ZDg3MGFlNmUyMzVhNjZkYjFlNWVlMTVhYTNhNDBmMDNmZmRkOWFiNjQ0YmJlNzEwNjc2MDg4YmRjNjVkMzk4MThhNmYxMzcyZTBmNzc0ZTkxMDUxMWMzNjk0MDY4NDA1NDVlZTVi",
    "TIEBA_SID": "H4sIAAAAAAAA_zIyNjMyNY43AQQAAP__hN3MzwgAAAA",
}

url = "https://tieba.baidu.com/c/f/frs/page_pc"
data = {
    "kw": "%E4%B8%89%E8%A7%92%E6%B4%B2%E8%A1%8C%E5%8A%A8",
    "pn": "3",
    "is_good": "0",
    "cid": "",
    "sort_type": "3",
    "tab_id": "1",
    "tab_type": "13",
    "tab_name": "热门",
    "forum_id": "27995444",
    "is_newfrs": "1",
    "is_newfeed": "1",
    "rn": "30",
    "rn_need": "10",
    "tbs": "00f796ea39582f881784194224",
    "subapp_type": "pc",
    "_client_type": "20",
    "sign": "fbefe99f964e8373ae319cd24131e6c1",
}

response = requests.post(url, headers=headers, cookies=cookies, data=data)
print(response.text)
