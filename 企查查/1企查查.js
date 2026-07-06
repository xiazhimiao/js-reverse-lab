var crypto_js = require('crypto-js')

var a_data = {
    "n": 20,
    "codes": {
        "0": "W",
        "1": "l",
        "2": "k",
        "3": "B",
        "4": "Q",
        "5": "g",
        "6": "f",
        "7": "i",
        "8": "i",
        "9": "r",
        "10": "v",
        "11": "6",
        "12": "A",
        "13": "K",
        "14": "N",
        "15": "k",
        "16": "4",
        "17": "L",
        "18": "1",
        "19": "8"
    }
}

function encrypt(e, t) {
    return crypto_js.HmacSHA512(e, t).toString();
}

function o_default() {
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var o = t[i].charCodeAt() % a_data.n;
        n += a_data.codes[o]
    }
    return n
}

function get_key() {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , n = JSON.stringify(e).toLowerCase();
    return encrypt(t + n, o_default(t)).toLowerCase().substr(8, 20)
}

function get_value() {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
        , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
        , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
        , i = JSON.stringify(e).toLowerCase();
    return encrypt(n + "pathString" + i + t, o_default(n))
}

function qcc_spider(page, tid) {
    var data = {
        "searchKey": "小米",
        "pageIndex": page,
        "pageSize": 20
    }
    var t = "/api/search/searchmulti"

    var i = get_key(t, data)
    var u = get_value(t, data, tid);  // 传递的第二个参数为网站的window.tid
    var headers = {}
    headers['key'] = i
    headers['val'] = u
    return headers
}


// console.log(qcc_spider(1));
// console.log(qcc_spider(1)['val'].length)