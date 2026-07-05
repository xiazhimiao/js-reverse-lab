R = global

function p_(t) {
    t = R["encodeURIComponent"](t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return o("0x" + t)
    });
    try {
        return R["btoa"](t)
    } catch (n) {
        return R[W5][K5](t)[U5](Z5)
    }
}

function o(n) {
    t = "",
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']["forEach"](function (n) {
            t += R["unescape"]("%u00" + n)
        });
    var t, e = t;
    return R["String"][e](n)
}

function h_(n, t) {
    t = t || u();
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++) n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n["join"]("")
}

/*a = [
    "36",
    "cn",
    "2026-07-01_2026-07-05",
    "all",
    3,
    "2026-07-01",
    "2026-07-05",
    3
]*/
// r = +new R["Date"] - (11634 || 0) - 1661224081041

// a = a["sort"]()["join"]("");
// a = p_(a);
// a = (a += "@#" + "/rank/release") + ("@#" + r) + ("@#" + 3);

// e = p_(h(a, "xyz517cda96efgh"))

function get_analysis(page) {
    var a = [
        "36",
        "cn",
        "2026-07-01_2026-07-05",
        "all",
        3,
        "2026-07-01",
        "2026-07-05",
        page
    ]
    a = a['sort']()['join']("")
    a = p_(a)
    r = +new R["Date"] - (576 || 0) - 1661224081041
    a = (a += "@#" + "/rank/offline") + ("@#" + r) + ("@#" + 3)
    d = "xyz517cda96efgh"
    e = p_(h_(a, d))
    return e
}
console.log(get_analysis(1));

// console.log(e)