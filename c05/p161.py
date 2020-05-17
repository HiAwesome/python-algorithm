def binarySearchWithRecursive(alist, item):
    if len(alist) == 0:
        return False

    mid = len(alist) // 2

    if alist[mid] == item:
        return True
    elif alist[mid] < item:
        return binarySearchWithRecursive(alist[mid + 1:], item)
    else:
        return binarySearchWithRecursive(alist[:mid], item)


if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binarySearchWithRecursive(test_list, 3))
    print(binarySearchWithRecursive(test_list, 13))

"""
False
True
"""
