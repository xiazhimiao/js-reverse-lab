const crypto = require('crypto');
const sm4 = require('sm-crypto').sm4;
const sm2 = require('sm-crypto').sm2;
const BigInt = require('big-integer');

// UUID生成函数
var generate_uuid = function () {
    const random_bytes = crypto.randomBytes(16);
    random_bytes[6] = (random_bytes[6] & 0x0F) | 0x40;
    random_bytes[8] = (random_bytes[8] & 0x3F) | 0x80;
    return [
        random_bytes.toString('hex', 0, 4),
        random_bytes.toString('hex', 4, 6),
        random_bytes.toString('hex', 6, 8),
        random_bytes.toString('hex', 8, 10),
        random_bytes.toString('hex', 10, 16)
    ].join('-');
}

// 查询参数转换函数
var getQueryString = function (t) {
    var e = "";
    for (var r in t) {
        var n = t[r];
        void 0 !== n && (e = e + r + "=" + encodeURIComponent(n) + "&")
    }
    return e.length > 0 ? e.substring(0, e.length - 1) : e;
}

// 参数排序和连接函数
var O = function (t) {
    var e = "";
    for (var r in t) {
        var n = t[r];
        "" !== n && null != n && (e = "".concat(e).concat(r, "=").concat(n, "&"))
    }
    return e.length > 0 ? e.substring(0, e.length - 1) : e;
};

// 参数排序函数
var getSortString = function (t) {
    var e = function (t) {
        var e = Object.keys(t).sort(), r = {};
        return e.forEach(function (e) {
            r[e] = t[e];
        }), r;
    }(t);
    return O(e);
};

// 签名函数
var signature = function (t, e, r, n) {
    return sm2.doSignature(t, e, {
        hash: !0,
        publicKey: r,
        userId: n
    });
};

// 大整数转换函数
var Yi = function (t) {
    return BigInt(t, 16).toString(10);
}

var Zi = function (t) {
    return "".concat(Yi(t.slice(0, t.length / 2)), ",").concat(Yi(t.slice(t.length / 2)));
}

// 加密配置
var e = {
    "appId": "27IGtFrNFDc",
    "signType": "SM2",
    "encryptType": "SM4",
    "appSignPrivateKey": "7faa61bb9051707ad9d9d2c417d61e038a3af871a61c8da534a9061ac1e51c32",
    "appSignPublicKey": "040f5940c99c46ee9e438487c6a41d880b93f0804ea0e5ef53a062bb08203fc2a675b3d2b7a9aeb1862bb1b8fa5d17a40e300cbbe9a470ee3bf89b4ccb1c899719",
    "encryptKey": "dbb78b8b64d640bb130255c69e959973",
    "platformPublicKey": "0475ed079f423c14c6cc2fec93ce296cefc96c4be11af343c3f654f99140f8d6861589308929156ae62a74955c8bb2f4af540a45c7d1208f2ca61b264b4f383e27"
};

// 主函数
function generateRequestPayload(page) {
    // 生成随机字符串和时间戳
    var nonceStr = generate_uuid().replace(/-/g, '');
    var timestamp = new Date().getTime();

    // 构建请求参数
    var params = {
        "param": "",
        "page": page,
        "size": 10
    };
    var i = getQueryString(params);
    var queryContent = sm4.encrypt(i, e.encryptKey);

    // 构建签名数据
    var n = {
        "version": "1.0",
        "appId": "27IGtFrNFDc",
        "signType": "SM2",
        "encryptType": "SM4",
        "nonceStr": nonceStr,
        "timestamp": timestamp,
        "queryContent": queryContent
    };

    // 生成签名
    var a = getSortString(n);
    var o = signature(a, e.appSignPrivateKey, e.appSignPublicKey, e.appId);
    n['sign'] = Zi(o);
    return n;
}

// 使用示例
// const payload = generateRequestPayload(1); // 可以传入page参数
// console.log(payload);