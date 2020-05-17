def quicksort(alist):
    quicksortHelper(alist, 0, len(alist) - 1)


def quicksortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quicksortHelper(alist, first, splitpoint - 1)
        quicksortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivot_value:
            leftmark += 1

        while alist[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    quicksort(alist)
    print(alist)

"""
[54, 26, 93, 17, 77, 31, 44, 55, 20]
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
