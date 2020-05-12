from timeit import Timer


def test1():
    """
    通过 += 添加元素
    """
    l = []
    for i in range(1000):
        l += [i]


def test2():
    """
    通过 append 添加元素
    """
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    """
    通过列表解析式
    引申知识点：Python 的列表解析式，集合解析式，字典解析式
    """
    l = [i for i in range(1000)]


def test4():
    """
    通过列表构造函数
    """
    l = list(range(1000))


if __name__ == '__main__':
    t1 = Timer("test1()", "from __main__ import test1")
    print("通过 += 添加元素执行 1000 次耗时", t1.timeit(number=1000), "秒")
    t2 = Timer("test2()", "from __main__ import test2")
    print("通过 append 添加元素执行 1000 次耗时", t2.timeit(number=1000), "秒")
    t3 = Timer("test3()", "from __main__ import test3")
    print("列表解析式执行 1000 次耗时", t3.timeit(number=1000), "秒")
    t4 = Timer("test4()", "from __main__ import test4")
    print("列表构造函数执行 1000 次耗时", t4.timeit(number=1000), "秒")

"""
通过 += 添加元素执行 1000 次耗时 0.10332232100000001 秒
通过 append 添加元素执行 1000 次耗时 0.06958381 秒
列表解析式执行 1000 次耗时 0.031555849 秒
列表构造函数执行 1000 次耗时 0.01182483199999998 秒
"""
