const crypto = require('crypto')

// A 函数 = MD5，原版 A(n, '', '') 后两个参数没用到，忽略
function A(str) {
    return crypto.createHash('md5').update(str, 'utf8').digest('hex')
}

// x 函数 = Object.assign polyfill，来自浏览器源码
var x = function () {
    return (x =
        Object.assign ||
        function (e) {
            for (var t, n = 1, r = arguments.length; n < r; n++)
                for (var o in (t = arguments[n]))
                    Object.prototype.hasOwnProperty.call(t, o) && (e[o] = t[o]);
            return e;
        }).apply(this, arguments);
}

function get_sign(e, t) {
    var n = '',
        r = [],
        o =
            t === 'pc'
                ? '36770b1f34c9bbf2e7d1a99d2b82fa9e'
                : [
                    'newwise',
                    'shoubai_ugc',
                    'smallapp',
                    'smallapp_weixin',
                    'smallapp_qq'
                ].includes(t)
                    ? '0039d79dc3cc2075129745a30237a3c4'
                    : 'tiebaclient!!!';
    for (var i in e) ['sign', 'sig'].includes(i) || r.push(i);
    return (
        (r = r.sort(function (e, t) {
            return e > t ? 1 : -1;
        })).forEach(function (t) {
            n += t + '=' + e[t];
        }),
            (n += o),
            x(x({}, e), {sign: A(n, '', '')})
    );
}

// 命令行: node Sign生成.js '{"kw":"python","_client_type":"20"}'
var data = JSON.parse(process.argv[2])
var subapp_type = data.subapp_type || 'pc'
var result = get_sign(data, subapp_type)
console.log(JSON.stringify(result))
