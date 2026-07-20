/**
 * 税务局 — 浏览器环境模拟 (补环境)
 *
 * 在 Node.js 中模拟浏览器 DOM/BOM API，
 * 使目标加密 JS 可以脱离浏览器执行。
 */

// ═══════════════════════════════════════════════════════════
//  日志
// ═══════════════════════════════════════════════════════════

_log = console.log;
let is_logging = true;

function v_log() {
    if (is_logging) {
        _log(...arguments);
    }
}

var _null = function () {
    v_log("--arguments--", ...arguments);
};

// ═══════════════════════════════════════════════════════════
//  代理工具 — 监听对象属性读写
// ═══════════════════════════════════════════════════════════

function getEnv(proxy_array) {
    for (let i = 0; i < proxy_array.length; i++) {
        handler = `{
            get: function(target, property, receiver) {
                   if(property === "removeChild") return target[property];
                   console.log('方法：get','    对象：${proxy_array[i]}','    属性：',property,'    属性类型：',typeof property,'    属性值类型：',typeof target[property]);
                   return target[property];
            },
            set: function(target, property, value, receiver){
                    console.log('方法：set','    对象：${proxy_array[i]}','    属性：',property,'    属性类型：',typeof property,'    属性值类型：',typeof target[property]);
                    return Reflect.set(...arguments);
            }
        }`;
        eval(`
            try {
                ${proxy_array[i]};
                ${proxy_array[i]} = new Proxy(${proxy_array[i]}, ${handler});
            } catch (e) {
                ${proxy_array[i]} = {};
                ${proxy_array[i]} = new Proxy(${proxy_array[i]}, ${handler});
            }
        `);
    }
}

// ═══════════════════════════════════════════════════════════
//  window
// ═══════════════════════════════════════════════════════════

window = globalThis;
window.top = window;
// window.localStorage = {
//     "$_YWTU": "8rllIvsIdx8PmHimw5jB1foGV8BOv6xtYx6vhKyiRC7",
//     "_$rc": "KJtbszghh0Yphb3B9bqmHw946DU6vLuVb6piMY82yAPXvHV3LPY5TvHbQoUNnCPqwdLs_G90h2quuRv5hNi5O9Hc5hRG_PucKtjs3dSLHC62AAdicK__.EozcLXn1Bszn771ATLXMjtSr3m6tPJgVF1IwPCNskc5pG83WDfvi.QXOtrcu16v89zSz7Bi3tmGCZAykhAOU13gf9Tk_DweOCvZ21X0ILE0Tm5.QWutYdEyYyAdVkWsDaA4qFFj6bJ0BckXHqOrJvgFOfv4_AgCxmYTZgJcB1JaFm03cmyjuTN_UCMRTrfdEKRa4pHsh6qStPHDeTtyGca6voLqXjcADd4AhS2bobP4ASRLp9wcgAQHSuXLQtmmFCDp_RB6wmyF.tVQDwFL740sJfIFnzIlI4NNGbdI7Xl6MCWPFIfnF047H36Bb0gLZkeisI8DTCioCQEGeG61u601sHFQsoeJT1Jnn_rHwNknMQycIxveh6ekj24P8KreugQPg3UTjv.BRofNpIphcnJaV2.jhnbE5m1Ln5IzVabSI3My_zdTVX7vaRQr_iL8cC1.PhWHy5fp1FxjtcjG4Dfso8FL3R8wTDQ5F6q4BwIed0DgCE_OhC17nwgj_rlEKlZNALgXaf2ITyrnANGz.7eYC21HUudTh8gGt_t_163YNvmjx_5OGzMYOUBuA0sr6ex46JE2yQuCXI2SMpNcLPBer9rTip6dxEtqe6JLiY5YWI2w7IsTmio8MjokztnM8RBKk_ndhXqcf2CIlq",
//     "sbqxDataBefoer_mh": "{\"val\":{\"sbqxMsg\":\"7月征期已结束，请关注下月征期\",\"sbqxzt\":\"N\"},\"exp\":1784544766050}",
//     "__#classType": "localStorage",
//     "$_YVTX": "Wsl"
// };
// window.sessionStorage = {
//     "$_YWTU": "8rllIvsIdx8PmHimw5jB1foGV8BOv6xtYx6vhKyiRC7",
//     "szzhDataBefore_mh": "{\"val\":{\"dpptUrl\":\"https://dppt.ningbo.chinatax.gov.cn:8443\",\"szzhUrl\":\"https://etax.ningbo.chinatax.gov.cn:8443\",\"ldjUrl\":\"https://etax.ningbo.chinatax.gov.cn/login-web/api/third/sso/login/function/integration?qd=kexin&channelId=web&tag=xdj&goto=20221213\"},\"exp\":1816077166055}",
//     "$_YVTX": "Wsl"
// };
// window.indexedDB = {};
window.addEventListener = _null;
window.ActiveXObject = undefined;

// ═══════════════════════════════════════════════════════════
//  navigator
// ═══════════════════════════════════════════════════════════

navigator = {
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    webdriver: false,
    languages: ['en-GB', 'zh-CN', 'zh'],
    platform: "Win32",
    webkitPersistentStorage: {},
};

// ═══════════════════════════════════════════════════════════
//  location
// ═══════════════════════════════════════════════════════════

location = {
    "ancestorOrigins": {},
    "href": "https://etax.ningbo.chinatax.gov.cn:8443/fPfqwdZo9U4c/ULtZPgcuAcwb.0515a6f.js",
    "origin": "https://etax.ningbo.chinatax.gov.cn:8443",
    "protocol": "https:",
    "host": "etax.ningbo.chinatax.gov.cn:8443",
    "hostname": "etax.ningbo.chinatax.gov.cn",
    "port": "8443",
    "pathname": "/fPfqwdZo9U4c/ULtZPgcuAcwb.0515a6f.js",
    "search": "",
    "hash": ""
};

// ═══════════════════════════════════════════════════════════
//  document
// ═══════════════════════════════════════════════════════════

div = {
    getElementsByTagName: function (arg) {
        _log(...arguments);
        if (arg === "i") {
            return [];
        }
    }
};

getAttribute = function () {
    if (arguments[0] === 'r') {
        return 'm';
    }
};

script_element = {
    getAttribute: getAttribute,
    parentElement: {
        removeChild: function () {
            console.log('script_element.parentElement.removeChild', arguments);
        }
    }
};

script = [
    script_element,
    script_element,
];

var content = "meta_content";
meta = {
    getAttribute: function (arg) {
        if (arg === "r") {
            return "m";
        }
    },
    parentNode: {
        removeChild: function () {
            _log("removeChild", ...arguments);
        }
    },
    content: content
};

document = {
    getElementById: function getElementById() {
        _log(arguments);
    },
    createElement: function (a) {
        _log(arguments);
        if (a === "div") {
            return div;
        }
        if (a === "form") {
            return {};
        }
    },
    getElementsByTagName: function (arg) {
        console.log("getElementsByTagName-->", arguments);
        if (arg === "script") {
            return script;
        }
        if (arg === "meta") {
            return [meta, meta];
        }
        if (arg === "base") {
            return {};
        }
    },
    addEventListener: _null,
    appendChild: _null,
    removeChild: _null,
    documentElement: {},
    characterSet: 'UTF-8',
    charset: 'UTF-8'
};

// ═══════════════════════════════════════════════════════════
//  定时器屏蔽
// ═══════════════════════════════════════════════════════════

setInterval = function () {};
setTimeout = function () {};

// ═══════════════════════════════════════════════════════════
//  代理监听 (按需启用)
// ═══════════════════════════════════════════════════════════

// getEnv(['window', 'document', 'location', 'navigator', 'history', 'screen']);
// getEnv(['window','document','meta']);

// ═══════════════════════════════════════════════════════════
//  目标代码占位 — Python 负责替换
// ═══════════════════════════════════════════════════════════

'encrypt_js_code';
'decrypt_js_run_code';

// ═══════════════════════════════════════════════════════════
//  结果导出
// ═══════════════════════════════════════════════════════════

function get_cookie() {
    return document.cookie;
}
