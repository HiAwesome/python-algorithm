def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos += 1

    return found


if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(orderedSequentialSearch(test_list, 3))
    print(orderedSequentialSearch(test_list, 13))

"""
False
True
"""
