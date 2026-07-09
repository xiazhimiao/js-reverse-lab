d = {
    'iRmDq': function (i, j) {
        return i(j);
    },
    'GQcTJ': function (i, j) {
        return i / j;
    },
    'wUWKM': function (i, j, k) {
        return i(j, k);
    },
    'Saaxu': function (i, j) {
        return i(j);
    }
}

function get_time(){
    return d['iRmDq'](parseInt, Math["round"](d["GQcTJ"](new Date()["getTime"](), 1000))["toString"]())
}
