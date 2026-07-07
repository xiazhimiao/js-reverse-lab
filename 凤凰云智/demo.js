require("./凤凰云智 - mod.js")

function r(e) {
    return e && e.__esModule ? e : {
        default: e
    }
}

n = window.loader
var a = r(n(954746));
var o = r(n(624362));
var i = r(n(896378));
var s = r(n(949284))
const l = {
    daily: o.default,
    zlg_daily: o.default,
    pre: i.default,
    zlg_pre: i.default,
    prod: s.default,
    zlg_prod: s.default
};
a.default.setMaxDigits(130);  // 这行代码不添加会导致整个js程序堵塞
const u = new a.default.RSAKeyPair("10001", "", l["prod"]);

console.log(a.default.encryptedString(u, encodeURIComponent(123)));