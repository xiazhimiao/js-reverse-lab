import time
import requests
from wasmtime import Store, Module, Instance, WasiConfig

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://spa14.scrape.center/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}

url = 'https://spa14.scrape.center/api/movie/'

# 加载wasm文件
store = Store()
with open("./scrape_center.wasm", "rb") as f:
    wasm_bytes = f.read()
module = Module(store.engine, wasm_bytes)
instance = Instance(store, module, [])

# 获取导出的encrypt函数
encrypt_func = instance.exports(store)["encrypt"]

for page in range(0, 2):
    offset = page * 10
    timestamp = int(time.time())
    # 调用wasm加密方法，传参offset、时间戳
    sign = encrypt_func(store, offset, timestamp)
    params = {
        "limit": "10",
        "offset": offset,
        "sign": sign
    }

    response = requests.get(url, headers=headers, params=params)
    print(response.json())
    print('-' * 30)