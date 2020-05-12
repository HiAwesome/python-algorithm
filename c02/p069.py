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


"""
为使用timeit模块，你需要创建一个Timer对象，这个对象的参数是两个Python语句。
第一个参数是你想进行计时的Python语句；第二个参数是建立这次测试你将要运行的语句。timeit模块就将测量运行这个语句一定次数多花费的时间。
如果不加要求，timeit模块的默认运行次数是一百万次。运行结束后，它将以浮点数的形式返回运行的总时间（单位：秒）。
你也可以在timeit中附上一个名叫number的参数，这样你就可以指定程序被执行的次数。
下图将展示对我们的每一个程序执行1000次，分别需要花费的时间。

在下面的实验中，我们进行测试的语句是调用函数到test1()，test2()，等等。
这个设置语句可能会让你感觉到十分奇怪，所以让我们更加细致的考虑它。
你可能对from，import语句十分熟悉，但这个语句常常被运用在Python程序文本的开头。
在这种情况下，from__main__importtest1这个语句将来自__main__命名空间的函数test1调用到为进行时间测量而建立的timeit命名空间中去。
Timeit模块这样做是以为它需要在某中特定的环境中运行，这种环境要求将你可能已经生成的，或已经偏离的，
或可能以某种不可预测的方式对你程序的运行产生干扰的变量进行整理。
"""

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
