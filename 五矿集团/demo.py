import execjs
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://ec.minmetals.com.cn",
    "Pragma": "no-cache",
    "Referer": "https://ec.minmetals.com.cn/open/home/purchase-info",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
cookies = {
    "SUNWAY-ESCM-COOKIE": "0f081060-5943-469c-9c4d-c4a884b529cd",
    "__jsluid_s": "24aa3a0c255633e0ac5cb2605c5a54be",
    "JSESSIONID": "B60F7911822D606336ED38B9A193B03C"
}


def get_public_key():
    url = "https://ec.minmetals.com.cn/open/homepage/public"
    response = requests.post(url, headers=headers, cookies=cookies)
    return response.text


def get_encrypt_param(public_key, page):
    with open('1五矿集团.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    return ctx.call('encrypt_param', public_key, page)


def get_info(param):
    url = "https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page"
    data = {
        "param": param
    }
    print(data)
    response = requests.post(url, headers=headers, cookies=cookies, json=data)
    print(response.text)


key = get_public_key()
encrypt_param = get_encrypt_param(key, 1)
get_info(encrypt_param)
