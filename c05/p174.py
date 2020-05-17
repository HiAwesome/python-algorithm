def bubblesort(alist):
    exchange_count = 0
    scan_count = 0

    for num in range(len(alist) - 1, 0, -1):
        scan_count += 1
        for i in range(num):
            if alist[i] > alist[i + 1]:
                exchange_count += 1
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

    print(exchange_count, scan_count)


if __name__ == '__main__':
    alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    print(alist)
    bubblesort(alist)
    print(alist)

"""
[20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
4 9
[20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
"""
