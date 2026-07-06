import re
import json
import requests

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs


class Qichacha:
    def __init__(self):
        self.url = 'https://www.qcc.com/web/search?key=%E5%B0%8F%E7%B1%B3'
        self.api_url = 'https://www.qcc.com/api/search/searchMulti'

        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }

        self.cookies = {
            "acw_tc": "781bad3917832472098638403e90f53639a73a95e58381b034162732c46ebd",
            "QCCSESSID": "a66cc9d9755448654670ba6d63",
            "qcc_did": "952ac01e-c56a-44a5-b21b-a20cc8dd7702",
            "UM_distinctid": "19f31d11f6f1ea3-00a6c10ef6125b8-4c657b58-1fa400-19f31d11f702413",
            "_c_WBKFRo": "Y5XZ2iv5uOopbJuJ89NyAbBXtEOadZVnndv76Yxf",
            "_nb_ioWEgULi": "",
            "CNZZDATA1254842228": "1319283656-1783247216-https%253A%252F%252Fcn.bing.com%252F%7C1783247290"
        }

    def get_all_id(self):
        params = {
            "key": "小米"
        }

        response = requests.get(self.url, headers=self.headers, cookies=self.cookies, params=params)
        tid = re.findall(r"window.tid='(.*?)'", response.text)[0]
        pid = re.findall(r"window.pid='(.*?)'", response.text)[0]
        # print(tid, pid)
        return tid, pid

    def get_company_info(self):
        with open('1企查查.js', encoding='utf-8') as f:
            js_code = f.read()

        js = execjs.compile(js_code)

        page = 1
        tid, pid = self.get_all_id()
        headers_info = js.call('qcc_spider', page, tid)

        # 复制以避免修改原字典
        api_headers = self.headers.copy()

        # 修改现有参数
        api_headers["accept"] = "application/json, text/plain, */*"
        api_headers["priority"] = "u=1, i"
        api_headers["sec-fetch-dest"] = "empty"
        api_headers["sec-fetch-mode"] = "cors"
        api_headers["sec-fetch-site"] = "same-origin"

        # 添加新参数
        api_headers["content-type"] = "application/json"
        api_headers["origin"] = "https://www.qcc.com"

        referer_url = "https://www.qcc.com/web/search?key=%E5%B0%8F%E7%B1%B3&p=1"
        api_headers["referer"] = referer_url
        api_headers["x-pid"] = pid
        api_headers["x-requested-with"] = "XMLHttpRequest"

        api_headers[headers_info['key']] = headers_info['val']

        data = {
            "searchKey": "小米",
            "pageIndex": page,
            "pageSize": 20
        }

        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(self.api_url, headers=api_headers, data=data, cookies=self.cookies)
        return response


if __name__ == '__main__':
    print(Qichacha().get_company_info().json())
