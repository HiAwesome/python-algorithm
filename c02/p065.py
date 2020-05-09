def anagram_solution2(s1, s2):
    """
    第一眼看上去你可能会认为这个算法的时间复杂度是 O(n), 毕竟排序后只需要一个简单的循环去比较 n 个字符。
    然而对 Python 内建的 sort 方法的两次使用并非毫无消耗。
    事实上，正如我们在后面的章节里将要看到的，排序方法的时间复杂度往往都是 o(n^2) 或者 O(nlogn),
    所以排序贡献了这个函数主要的循环操作。
    最终，这个算法和排序的时间复杂度相同。

    :param s1: 字符串1
    :param s2: 字符串2
    :return: 两个字符串是否为回文对应关系的布尔值
    """
    list1, list2 = list(s1), list(s2)
    list1.sort()
    list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            matches = False

    return matches


print(anagram_solution2('abcd', 'dcba'))

"""
True
"""
