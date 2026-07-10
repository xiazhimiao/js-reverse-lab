import os
import json
import tempfile
import requests
import subprocess

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.jianyu360.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.jianyu360.cn/jylab/supsearch/index.html?searchGroup=1",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
cookies = {
    "SESSIONID": "2cd76d2ff71447cec7d61594eed0eddff30027fe",
    "JYGuestUID": "1948637385000484864",
    "fid": "c76ea8e319a41fcde945d47d97416cb6",
    "JYTrustedId": "F1hGCwRMVwMADBVbQQgGEFcJBQAQW0cKXEMGAQdWFllaRE9FCwQJA0dYQ1ZQRAIABQ1AV0Za",
    "limitSearchTextFlag": "xinoA1753426332756453295",
    "Hm_lvt_52c42de35032567eb9d7a24a43c84bda": "1753426332,1753605523",
    "HMACCOUNT": "BB7C66DF142F5466",
    "Hm_lpvt_52c42de35032567eb9d7a24a43c84bda": "1753605634",
    "eid": "gGOp+K19f0pc6AzNCo2hoWATEKv3oIQii/kffbLd+IAx6JGwUKA6GxOqHJurqgb1JTWI1L4yaGW6qJ/WO6CNNQjS/sN8fkkDbSF+aRWazgE6lIYSy1SLQzRofLqbjAQNeOXBS4ELBTxCriXtE3wsf0XzfZabbBnhcqXX+XOT4Vw="
}
url = "https://www.jianyu360.cn/jyapi/jybx/core/fType/searchList"
data = {
    "searchGroup": 1,
    "reqType": "lastNews",
    "pageNum": 1,
    "pageSize": 50,
    "keyWords": "",
    "searchMode": 0,
    "bidField": "",
    "publishTime": "1722078161-1753614161",
    "selectType": "title,content",
    "subtype": "",
    "exclusionWords": "",
    "buyer": "",
    "winner": "",
    "agency": "",
    "industry": "",
    "province": "",
    "city": "",
    "district": "",
    "buyerClass": "",
    "fileExists": "",
    "price": "",
    "buyerTel": "",
    "winnerTel": ""
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)
# print(response.text)
encrypt_data = response.json()['data']
secret_key = response.json()['secretKey']

# 通过临时文件传递响应数据与密钥
with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
    json.dump({'encrypt_data': encrypt_data, 'secret_key': secret_key}, f)
    temp_path = f.name

# 执行js脚本
try:
    result = subprocess.run(['node', '剑鱼标讯.js', temp_path],
                            capture_output=True,
                            text=True,
                            encoding='utf-8')
    print(result.stdout)
finally:
    os.unlink(temp_path)  # 删除临时文件
