def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


if __name__ == '__main__':
    test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(test_list, 3))
    print(sequentialSearch(test_list, 13))

"""
False
True
"""
