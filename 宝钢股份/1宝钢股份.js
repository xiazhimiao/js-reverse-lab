var crypto_js = require("crypto-js")

function l(e) {
    for (var n = [], t = Array.of("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), a = 0; a < e; a++) {
        var c = Math.floor(10 * Math.random());
        n[a] = t[c]
    }
    return n.join("")
}

function s() {
    return parseInt((new Date).getTime() / 1e3)
}


function get_data(num) {
    var e = {}
    e.data = {
        "pageNo": num,
        "pageSize": 12,
        "condition": {
            "nodeId": 436
        }
    }
    var n = l(10)
        , t = s()
        , a = crypto_js.MD5(JSON.stringify(e.data ? e.data : "")).toString()
        , c = ""
        , o = "0/56f5cff3cad14853a44782c2c689ab2a"
        , i = "13ade1de1eff43ffb821735f352a4148";
    e["x-user"] = o,
        e["x-nonce"] = n,
        e["x-date"] = t,
        e["Content-Md5"] = a,
        c = "".concat("POST", "\n").concat("/v1/web/api/content/list?domainId=12", "\nx-user:").concat(o, "\nx-nonce:").concat(n, "\nx-date:").concat(t, "\nContent-Md5:").concat(a, "\n");
    var u = crypto_js.HmacSHA1(c, i).toString().toUpperCase();
    e["x-signature"] = u
    return e
}

// console.log(get_data(1));