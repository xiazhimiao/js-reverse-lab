import requests


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "app-guestid": "4B76575B2151307351B43CA7AA93AF6E",
    "app-version": "0",
    "content-type": "application/json",
    "data-label": "2026062401",
    "data-version": "1",
    "origin": "https://hangzhou.qccqcc.com",
    "priority": "u=1, i",
    "qcc-pc-referer": "https://hangzhou.qccqcc.com/",
    "referer": "https://hangzhou.qccqcc.com/",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Microsoft Edge\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0"
}
url = "https://newopenapiweb.17qcc.com/api/services/app/SearchFactory/GetPageList"
data = '{"KM":"6E30EC73609E7C2D4CD80DCE2DE87642","Ver":"1","Content":"7da46e20d8d31f36d127090185faba7c42d8bd68b81757ec2ba1243b47d58c889712161ef4247a4aa459029ab0548d6a1e6bc74d6c38938479be5c8d2dc54629d4ec19b6b821bb96371fc7b1ef7a19ab8aec211aa68acc3de5ddd54d0d5e4f4dc9fbd03eaae5faa3f6f1dea69469967d15407a594d8bffbaa761c3eaf4f8786e","Sign":"Ghq__\\\\"`BJpm[ST`=3y@\\u0021{qI@{km w%7hHz\\\\\\\\Z a[~=iLp@&&p^ZZ~|q&JR/LqN5\\\\\\\\X\\\\\\\\[tA,C95vs~Z&y.Nn|o^rap&RAE|Z=~inE{ZWYqAy mDHt{uky@e0DU?jfH9;t.|+fN=l@sUs5JdM~^}`\\u0021+@L$VtHiX+voU tp `=Hr\\\\\\\\LewA","RsaPubAes":"kMqqF8QaHwWFbKR4DQvqgO9/0bN5wKwKd6ndT2u31xgI5grK5mfHZpBHHim0LH7cM+8vm5cG8lBZgH+iqDrSLlEMKBeevCH4udywOtUoiF222eQUeuLjsmDKAyGTyodzCn8XCDuHCgkpmGDtoE5D3KFAZuFzifJXJsZTf695nL0=","IV":"Qj3gC9CrfJCuqT2q","TimesTamp":"8472ABCAE3D6E52AD1FAE5D67BFB2272"}'.encode('unicode_escape')
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)