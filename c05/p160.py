def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        # 这里用了地板除，只取结果的整数部分
        mid = (first + last) // 2
        if alist[mid] == item:
            found = True
        elif alist[mid] < item:
            first = mid + 1
        else:
            last = mid - 1

    return found


if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binarySearch(test_list, 3))
    print(binarySearch(test_list, 13))

"""
False
True
"""
