require("./mod.js")
u = window.loader("7d92")

var c = ["/pss/pw/web/cfc/getLoginQrcode", "/pss/pw/web/cfc/pollQrcodeStatus", "/base/api/appVersion/findDownloadPageInfo", "/nthl/api/dic/queryAdmdvsTree", "/pss/web/empUser/login", "/drugdcla/api/emtpCrtf/queryDrugEmtpCrtfExist", "/nthl/outMed/selectCityOfPoolareaOpenInfoList", "/base/api/drugOptins/queryDialog"];

function get_headers(page) {
    var e = {
        "transformRequest": {},
        "transformResponse": {},
        "timeout": 30000,
        "xsrfCookieName": "XSRF-TOKEN",
        "xsrfHeaderName": "X-XSRF-TOKEN",
        "maxContentLength": -1,
        "headers": {
            "common": {
                "Accept": "application/json, text/plain, */*"
            },
            "delete": {},
            "get": {},
            "head": {},
            "post": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "put": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "patch": {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        },
        "withCredentials": false,
        "baseURL": "/ebus/fuwu/api",
        "method": "post",
        "url": "/nthl/api/CommQuery/queryFixedHospital",
        "data": {
            "addr": "",
            "regnCode": "430100",
            "medinsName": "",
            "medinsLvCode": "",
            "medinsTypeCode": "",
            "outMedOpenFlag": "",
            "pageNum": page,
            "pageSize": 10,
            "queryDataSource": "es"
        }
    }

    e.headers.Accept = "application/json";
    e.headers["Content-Type"] = "application/json";
    e.headers.channel = "web";
    e.url.indexOf("userPerson/queryPsnInfo") > -1 && (e.headers.appid = "19E179E5DC29C05E65B90CDE57A1C7E5");
    var t = false;
    t && (e.headers.accessToken = t);
    var n = false;
    return e.url.indexOf("empUser/logout") > -1 && n && (e.headers.refreshToken = n),
        c.includes(e.url) ? e.data = {
            data: e.data || {}
        } : e = Object(u.a)(e),
        e
}

console.log('headers - >', get_headers(1));