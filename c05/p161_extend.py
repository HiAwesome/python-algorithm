"""
使用Python数组切片可能会带来额外的计算消耗，所以优化方法参数带上索引
"""


def binarySearchWithRecursiveAndIndex(alist, first, last, item):
    # 这里需要加上条件，限制 first <= last
    if len(alist) == 0 or first > last:
        return False

    mid = (first + last) // 2

    if alist[mid] == item:
        return True
    elif alist[mid] < item:
        return binarySearchWithRecursiveAndIndex(alist, mid + 1, last, item)
    else:
        return binarySearchWithRecursiveAndIndex(alist, first, mid - 1, item)


if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binarySearchWithRecursiveAndIndex(test_list, 0, len(test_list) - 1, 3))
    print(binarySearchWithRecursiveAndIndex(test_list, 0, len(test_list) - 1, 13))

"""
False
True
"""
