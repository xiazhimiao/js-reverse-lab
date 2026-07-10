const crypto_js = require("crypto-js");


R = function R(n) {
    for (var e = [8, 13, 18, 23], t = 0; t < e.length; t++)
        n = n.slice(0, e[t]) + "-" + n.slice(e[t]);
    return n;
}

c = function (e) {
    return crypto_js.MD5(e).toString()
}

N = function N() {
    for (var n = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "", e = [], t = "0123456789abcdef", r = 0; r < 36; r++) {
        var o = Math.floor(16 * Math.random());
        e[r] = t.substring(o, o + 1);
    }
    e[14] = "4";
    var u = 3 & Number(e[19]) | 8;
    e[19] = t.substring(u, u + 1),
        e[8] = e[13] = e[18] = e[23] = "-";
    var i = e.join("")
        , a = R(c(i + new Date().getTime() + n));
    return a;
}

var r = ""

function encrypt_message_id() {
    return N(r);
}

// console.log(encrypt_message_id())

M = function M(n, e, t, r, o, u, i, a, s, f) {
    var d = "987EBBF8450544D7A52D5539DF9A92A2"
        , l = "";
    return l = s ? "AppVersion=".concat(u, "Authorization=").concat(s, "Channel=").concat(i, "ClientType=").concat(o, "DeviceManufacture=").concat(t, "DeviceModel=").concat(r, "MessageId=").concat(a, "OsVersion=").concat(e, "Timestamp=").concat(n, "AppKey=").concat(d, "Url=").concat(f) : "AppVersion=".concat(u, "Channel=").concat(i, "ClientType=").concat(o, "DeviceManufacture=").concat(t, "DeviceModel=").concat(r, "MessageId=").concat(a, "OsVersion=").concat(e, "Timestamp=").concat(n, "AppKey=").concat(d, "Url=").concat(f),
        l = c(l.replace(/\s*/g, "")).substring(4, 28).toLocaleUpperCase();
}

function encrypt_signature(timestamp, message_id) {
    return M(timestamp, "iOS 10.0.1", "devtools", "iPhone 12/13 (Pro)", "5", "3.5.6", "bdw", message_id, undefined, encodeURIComponent("https://api.betterwood.com/base/app/store/listV2".split("betterwood.com")[1].split("?")[0]))
}

// console.log(encrypt_message_id())
// console.log(encrypt_signature())

function get_headers_info() {
    var timestamp = Date.now();
    var message_id = encrypt_message_id();
    return {
        'messageid': message_id,
        'signature': encrypt_signature(timestamp, message_id),
        'timestamp': timestamp,
    }
}

