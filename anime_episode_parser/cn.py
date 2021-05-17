_CN_NUM = {
    "〇": 0,
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "零": 0,
    "壹": 1,
    "贰": 2,
    "叁": 3,
    "肆": 4,
    "伍": 5,
    "陆": 6,
    "柒": 7,
    "捌": 8,
    "玖": 9,
    "貮": 2,
    "两": 2,
}

_CN_UNIT = {
    "十": 10,
    "拾": 10,
    "百": 100,
    "佰": 100,
    "千": 1000,
    "仟": 1000,
    "万": 10000,
    "萬": 10000,
}


def chinese_to_arabic(cn: str) -> int:
    """
    https://blog.csdn.net/hexrain/article/details/52790126
    :type cn: str
    :rtype: int
    """

    unit = 0  # current
    l_dig = []  # digest
    for cn_dig in reversed(cn):
        if cn_dig in _CN_UNIT:
            unit = _CN_UNIT[cn_dig]
            if unit == 10000 or unit == 100000000:
                l_dig.append(unit)
                unit = 1
        else:
            dig = _CN_NUM[cn_dig]
            if unit:
                dig *= unit
                unit = 0
            l_dig.append(dig)
    if unit == 10:
        l_dig.append(10)
    val, tmp = 0, 0
    for x in reversed(l_dig):
        if x == 10000 or x == 100000000:
            val += tmp * x
            tmp = 0
        else:
            tmp += x
    val += tmp
    return val
