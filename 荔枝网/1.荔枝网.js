delete global;

function Window() {
}

window = new Window()
self = window
self.self = window

Location = function Location() {
}
Location.prototype = {
    "ancestorOrigins": {},
    "href": "https://gdtv.cn/channels/2",
    "origin": "https://gdtv.cn",
    "protocol": "https:",
    "host": "gdtv.cn",
    "hostname": "gdtv.cn",
    "port": "",
    "pathname": "/channels/2",
    "search": "",
    "hash": "",
    /*toString() {
        return 'https://gdtv.cn/channels/2'
    }*/

}
location = new Location()

window.location = location

document = {
    toString() {
        return '[object HTMLDocument]'
    },
    location: window.location
}
window.document = document

// 代理监控 proxy: window.location与window.document也需要单独检测
/*function getEnv(proxy_array) {
    for (let i = 0; i < proxy_array.length; i++) {
        handler = `{
            get: function(target, property, receiver) {
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
proxy_array = ['window', 'document', 'location', 'navigator', 'history', 'screen', 'window.document', 'window.location']
getEnv(proxy_array);*/

var fs = require('fs');
var wasm_code = fs.readFileSync('lizhi.wasm');

var H = 128;
var c = null;
var M = new Array(128).fill(void 0);

M.push(void 0, null, !0, !1);

function E(A, g, I) {
    return E = function () {
        if ("undefined" == typeof Reflect || !Reflect.construct)
            return !1;
        if (Reflect.construct.sham)
            return !1;
        if ("function" == typeof Proxy)
            return !0;
        try {
            return Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], (function () {
                }
            ))),
                !0
        } catch (A) {
            console.log("E函数中的异常:::", A)
            return !1
        }
    }() ? Reflect.construct.bind() : function (A, g, I) {
        var B = [null];
        B.push.apply(B, g);
        var Q = new (Function.bind.apply(A, B));
        return I && D(Q, I.prototype),
            Q
    }
        ,
        E.apply(null, arguments)
}

function S() {
    for (var A = arguments.length, g = new Array(A), I = 0; I < A; I++)
        g[I] = arguments[I];
    var B = function () {
        try {
            return E(P, g)
        } catch (A) {
            console.log("S函数中的异常:::", A)
            return function () {
                return null
            }
        }
    }();
    return B.toString = function () {
        return ""
    }
        ,
        B
}

var N = new TextDecoder("utf-8", {
    ignoreBOM: !0,
    fatal: !0
})

function K(A, g) {
    return A >>>= 0,
        N.decode(k().subarray(A, A + g))
}

function t() {
    var g = {
        wbg: {}
    };
    return g.wbg.__wbindgen_object_drop_ref = function (A) {
        G(A)
    }
        ,
        g.wbg.__wbg_self_1ff1d729e9aae938 = function () {
            return R((function () {
                    return Y(self.self)
                }
            ), arguments)
        }
        ,
        g.wbg.__wbg_window_5f4faef6c12b79ec = function () {
            return R((function () {
                    return Y(window.window)
                }
            ), arguments)
        }
        ,
        g.wbg.__wbg_globalThis_1d39714405582d3c = function () {
            return R((function () {
                    return Y(globalThis.globalThis)
                }
            ), arguments)
        }
        ,
        g.wbg.__wbg_global_651f05c6a0944d1c = function () {
            return R((function () {
                    return Y(A.global)
                }
            ), arguments)
        }
        ,
        g.wbg.__wbindgen_is_undefined = function (A) {
            return void 0 === i(A)
        }
        ,
        g.wbg.__wbg_newnoargs_581967eacc0e2604 = function (A, g) {
            return Y(S(K(A, g)))
        }
        ,
        g.wbg.__wbg_call_cb65541d95d71282 = function () {
            return R((function (A, g) {
                    return Y(i(A).call(i(g)))
                }
            ), arguments)
        }
        ,
        g.wbg.__wbindgen_object_clone_ref = function (A) {
            return Y(i(A))
        }
        ,
        g.wbg.__wbg_instanceof_Window_9029196b662bc42a = function (A) {
            var g;
            try {
                g = i(A) instanceof Window
            } catch (A) {
                console.log("t函数中的异常:::", A)
                g = !1
            }
            return g
        }
        ,
        g.wbg.__wbg_document_f7ace2b956f30a4f = function (A) {
            var g = i(A).document;
            return U(g) ? 0 : Y(g)
        }
        ,
        g.wbg.__wbg_location_56243dba507f472d = function (A) {
            return Y(i(A).location)
        }
        ,
        g.wbg.__wbg_host_15090f3de0544fea = function () {
            return R((function (A, g) {
                    var I = L(i(g).host, w.__wbindgen_export_0, w.__wbindgen_export_1)
                        , B = h;
                    s()[A / 4 + 1] = B,
                        s()[A / 4 + 0] = I
                }
            ), arguments)
        }
        ,
        g.wbg.__wbg_origin_50aa482fa6784a0a = function () {
            return R((function (A, g) {
                    var I = L(i(g).origin, w.__wbindgen_export_0, w.__wbindgen_export_1)
                        , B = h;
                    s()[A / 4 + 1] = B,
                        s()[A / 4 + 0] = I
                }
            ), arguments)
        }
        ,
        g.wbg.__wbg_href_d62a28e4fc1ab948 = function () {
            return R((function (A, g) {
                    var I = L(i(g).href, w.__wbindgen_export_0, w.__wbindgen_export_1)
                        , B = h;
                    s()[A / 4 + 1] = B,
                        s()[A / 4 + 0] = I
                }
            ), arguments)
        }
        ,
        g.wbg.__wbg_newwithargs_a0432b7780c1dfa1 = function (A, g, I, B) {
            return Y(S(K(A, g), K(I, B)))
        }
        ,
        g.wbg.__wbindgen_string_new = function (A, g) {
            return Y(K(A, g))
        }
        ,
        g.wbg.__wbg_call_01734de55d61e11d = function () {
            return R((function (A, g, I) {
                    return Y(i(A).call(i(g), i(I)))
                }
            ), arguments)
        }
        ,
        g.wbg.__wbindgen_string_get = function (A, g) {
            var I = i(g)
                , B = "string" == typeof I ? I : void 0
                , Q = U(B) ? 0 : L(B, w.__wbindgen_export_0, w.__wbindgen_export_1)
                , C = h;
            s()[A / 4 + 1] = C,
                s()[A / 4 + 0] = Q
        }
        ,
        g.wbg.__wbg_eval_8c72ad5eafe427f2 = function () {
            return R((function (A, g) {
                    return Y(x(K(A, g)))
                }
            ), arguments)
        }
        ,
        g.wbg.__wbindgen_typeof = function (A) {
            return Y(I(i(A)))
        }
        ,
        g.wbg.__wbindgen_boolean_get = function (A) {
            var g = i(A);
            return "boolean" == typeof g ? g ? 1 : 0 : 2
        }
        ,
        g.wbg.__wbg_new_56693dbed0c32988 = function () {
            return Y(new Map)
        }
        ,
        g.wbg.__wbg_set_bedc3d02d0f05eb0 = function (A, g, I) {
            return Y(i(A).set(i(g), i(I)))
        }
        ,
        g.wbg.__wbindgen_number_new = function (A) {
            return Y(A)
        }
        ,
        g.wbg.__wbg_new0_c0be7df4b6bd481f = function () {
            return Y(new Date)
        }
        ,
        g.wbg.__wbg_getTime_5e2054f832d82ec9 = function (A) {
            return i(A).getTime()
        }
        ,
        g.wbg.__wbg_new_cd59bfc8881f487b = function (A) {
            return Y(new Date(i(A)))
        }
        ,
        g.wbg.__wbg_getTimezoneOffset_8aee3445f323973e = function (A) {
            return i(A).getTimezoneOffset()
        }
        ,
        g.wbg.__wbindgen_throw = function (A, g) {
            throw new Error(K(A, g))
        }
        ,
        g
}

var J = null;

function k() {
    return null !== J && 0 !== J.byteLength || (J = new Uint8Array(w.memory.buffer)),
        J
}

function s() {
    return null !== c && 0 !== c.byteLength || (c = new Int32Array(w.memory.buffer)),
        c
}

function U(A) {
    return null == A
}

function i(A) {
    return M[A]
}

var o = M.length;

function Y(A) {
    o === M.length && M.push(M.length + 1);
    var g = o;
    return o = M[g],
        M[g] = A,
        g
}

var P = Function
x = eval

function R(A, g) {
    try {
        return A.apply(this, g)
    } catch (A) {
        console.log("R函数中的异常:::", A)
        w.__wbindgen_export_3(Y(A))
    }
}

function L(A, g, I) {
    if (void 0 === I) {
        var B = y.encode(A)
            , Q = g(B.length, 1) >>> 0;
        return k().subarray(Q, Q + B.length).set(B),
            h = B.length,
            Q
    }
    for (var C = A.length, E = g(C, 1) >>> 0, D = k(), w = 0; w < C; w++) {
        var M = A.charCodeAt(w);
        if (M > 127)
            break;
        D[E + w] = M
    }
    if (w !== C) {
        0 !== w && (A = A.slice(w)),
            E = I(E, C, C = w + 3 * A.length, 1) >>> 0;
        var i = k().subarray(E + w, E + C);
        E = I(E, C, w += F(A, i).written, 1) >>> 0
    }
    return h = w,
        E
}

function G(A) {
    var g = i(A);
    return function (A) {
        A < 132 || (M[A] = o,
            o = A)
    }(A),
        g
}

B = t()

function get_encrypt_headers() {
    // 自行创建对象
    WebAssembly.instantiate(wasm_code, B).then(ret => {
        // C与w值不能加var, 让这两个变量作为全局变量
        C = ret.instance;
        w = C.exports;

        function encrypt_data(A, g, I, B, Q, C) {
            try {
                var E = L(A, w.__wbindgen_export_0, w.__wbindgen_export_1)
                    , D = h
                    , i = L(g, w.__wbindgen_export_0, w.__wbindgen_export_1)
                    , o = h
                    , Y = L(I, w.__wbindgen_export_0, w.__wbindgen_export_1)
                    , N = h
                    , J = L(B, w.__wbindgen_export_0, w.__wbindgen_export_1)
                    , k = h
                    , K = L(Q, w.__wbindgen_export_0, w.__wbindgen_export_1)
                    , y = h;
                return G(w.a(E, D, i, o, Y, N, J, k, K, y, function (A) {
                    if (1 == H)
                        throw new Error("out of js stack");
                    return M[--H] = A,
                        H
                }(C)))
            } finally {
                M[H++] = void 0
            }
        }

        var result = encrypt_data(
            "GET",
            "https://gdtv-api.gdtv.cn/api/channel/v1/channel/2",
            "WEB_742c7830-99e4-11f0-a76b-e9c42945e494",
            "WEB_PC",
            "",
            undefined
        )

        // 将map对象转为普通对象
        var headers_obj = Object.fromEntries(result);
        // 将obj对象转为字符串
        var json_str = JSON.stringify(headers_obj);
        console.log(json_str)
    })
}

get_encrypt_headers();
