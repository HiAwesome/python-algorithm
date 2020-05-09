def anagram_solution1(s1, s2):
    """
    两个 while 循环表示此算法的时间复杂度是 O(n^2).

    :param s1: 字符串1
    :param s2: 字符串2
    :return: 两个字符串是否为回文对应关系的布尔值
    """
    a_list = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False

        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok


print(anagram_solution1('abcd', 'dcba'))

"""
True
"""
