"""
因为冒泡排序必须要在最终位置找到之前不断交换数据项，所以它经常被认为是最低效的排序方法。
这些“浪费式”的交换操作消耗了许多时间。但是，由于冒泡排序要遍历整个未排好的部分，它可以做一些大多数排序方法做不到的事。
尤其是如果在整个排序过程中没有交换，我们就可断定列表已经排好。因此可改良冒泡排序，使其在已知列表排好的情况下提前结束。
这就是说，如果一个列表只需要几次遍历就可排好，冒泡排序就占有优势：它可以在发现列表已排好时立刻结束。
代码2就是改良版冒泡排序。它通常被称作“短路冒泡排序”。

https://stackoverflow.com/a/40309322

短路冒泡排序实际上降低了扫描的次数。
"""


def shortBubbleSort(alist):
    exchange_count = 0
    scan_count = 0
    exchanges = True
    passnum = len(alist) - 1

    while passnum > 0 and exchanges:
        exchanges = False
        scan_count += 1
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange_count += 1
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

        passnum -= 1

    print(exchange_count, scan_count)


if __name__ == '__main__':
    # 这个测试用例只需要把 90 不断向后交换四个位置，因此第二次扫描时 exchanges 就保持为 False，程序判断排序已完成
    alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    print(alist)
    shortBubbleSort(alist)
    print(alist)

"""
[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
4 2
[20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
"""
