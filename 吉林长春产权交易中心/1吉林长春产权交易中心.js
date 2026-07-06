var g = function () {
    function e() {
        this.codeStr = "",
            this.pubPass = "BX1o65CoobwcDP33iQW6ld1OyIPsNzF1",
            this.pubPassNum = [],
            this.publicKey = "",
            this.setPass(this.pubPass)
    }

    return e.prototype.encode = function (e) {
        var t = "";
        try {
            t = JSON.stringify(e)
        } catch (n) {
            return console.error(n + "这不是一个正确的json对象"),
                ""
        }
        return this.encryptCode(t)
    }
        ,
        e.prototype.decode = function (e) {
            var t;
            try {
                t = JSON.parse(this.decryptCode(e))
            } catch (n) {
                return void console.error(n + "json对象转出失败")
            }
            return t
        }
        ,
        e.prototype.encryptCode = function (e) {
            for (var t = encodeURI(e), n = [], i = 0, r = "", o = this.random(16, 32), a = this.randomStr(o), s = this.stringChangeASCIINumberArrs(a), l = 0, c = 0, u = 0, h = 0; h < t.length; h++)
                i = t.charCodeAt(h),
                l == this.pubPassNum.length && (l = 0),
                    i += this.pubPassNum[l],
                    l++,
                c == s.length && (c = 0),
                    i += s[c],
                    c++,
                    u += i,
                u > 65535 && (u -= 65535),
                    r = i.toString(36),
                    r = ("00" + r).substr(-2, 2),
                1 == r.length && (r = "0" + r),
                    n.push(r);
            var d = "";
            return d = u.toString(36),
                d = ("0000" + r).substr(-4, 4),
                n.unshift(a),
                n.unshift(o.toString(36)),
                n.unshift(d),
                n.join("")
        }
        ,
        e.prototype.decryptCode = function (e) {
            var t = ""
                , n = 0
                , i = ""
                , r = []
                , o = []
                , a = 0
                , s = 0;
            t = e.substr(4, 1),
                n = parseInt(t, 36),
                i = e.substr(5, n),
                r = this.stringChangeASCIINumberArrs(i),
                t = e.substr(5 + n, e.length - 5 - n);
            for (var l = "", c = 0, u = 0, h = 0; h < t.length / 2; h++)
                l = t.substr(u, 2),
                    u += 2,
                    c = parseInt(l, 36),
                s == r.length && (s = 0),
                    c -= r[s],
                    s++,
                a == this.pubPass.length && (a = 0),
                    c -= this.pubPassNum[a],
                    a++,
                    l = String.fromCharCode(c),
                    o.push(l);
            return t = o.join(""),
                t = decodeURI(t),
                t
        }
        ,
        e.prototype.setPass = function (e) {
            this.pubPassNum = this.stringChangeASCIINumberArrs(e)
        }
        ,
        e.prototype.stringChangeASCIINumberArrs = function (e) {
            for (var t = [], n = 0; n < e.length; n++)
                t.push(e.charCodeAt(n));
            return t
        }
        ,
        e.prototype.random = function (e, t) {
            return void 0 === e && (e = 0),
            void 0 === t && (t = 1e4),
                Math.floor(Math.random() * (t - e) + e)
        }
        ,
        e.prototype.randomStr = function (e) {
            for (var t = [], n = 0; n < e; n++)
                t.push(this.random(0, 35).toString(36));
            return t.join("")
        }
        ,
        e
}()


function get_payload(payload) {
    var aes = new g;
    // var a = JSON.stringify(o), s = this.aes.encode(a), l = this.opt.headers;
    return aes.encode(JSON.stringify(payload));
}

function get_data(response) {
    var aes = new g;
    return aes.decode(response);
}


// console.log(get_payload({
//     "id": "rtvg4qbdhioxgp8x",
//     "projectKey": "honsan_cloud_ccprec",
//     "clientKey": "rtvg3h42e00xrl6i",
//     "token": null,
//     "clientDailyData": {},
//     "acts": [{
//         "id": "rtvg4q5kidcsdbx2",
//         "fullPath": "/ccprec.com.cn.web/client/info/cqweb_nonphy_cqzr",
//         "args": [1, 20, null]
//     }]
// }))