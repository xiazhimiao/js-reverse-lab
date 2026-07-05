// s.Fk(a.Z({}, n, s.xZ()))

/*
k = function (n, t) {
    var r = Date.now().toString()
        , e = a()(r + "9527" + r.substr(0, 6))
        , o = t;
    o || (o = f()().get("next-i18next") || f()().get("language"));
    var i = {
        code: e,
        timestamp: r,
        platform: "web_pc",
        v: "0.1.0",
        mytoken: null !== n && void 0 !== n ? n : f()().get("mytoken_sid")
    };
    return o && (i.language = (0,
        l.m)(o)),
        i
}*/
var crypto_js = require('crypto-js')

function get_md5(text) {
    return crypto_js.MD5(text).toString();
}

function get_params() {
    var t = Date.now().toString();
    var code = get_md5(t + "9527" + t.substr(0, 6))
    return {
        time: t,
        code: code
    }
}

console.log(get_params());

