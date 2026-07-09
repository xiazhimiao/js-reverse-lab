import time
import execjs
import requests
from wasmtime import Store, Module, Instance

# 加载wasm文件（替换原pywasm.load）
store = Store()
with open("./encrypt.wasm", "rb") as f:
    wasm_bin = f.read()
module = Module(store.engine, wasm_bin)
instance = Instance(store, module, [])
encrypt_func = instance.exports(store)["encrypt"]

# 加载JS
with open('1.码上爬.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.mashangpa.com/problem-detail/11/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0": "1783596329",
    "HMACCOUNT": "4BE437411185BD72",
    "sessionid": "j4nhamqhzyv576movif9zm150hlhn1lr",
    "Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0": "1783596552"
}
url = "https://www.mashangpa.com/api/problem-detail/11/data/"

for page in range(1, 2):
    result = ctx.call('get_time')
    # 替换 runtime.exec('encrypt', [page, result])
    m = encrypt_func(store, page, result)
    params = {
        "page": page,
        "m": m,
        "_ts": result
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    print(response.json())