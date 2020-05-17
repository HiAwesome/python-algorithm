def shellSort(alist):
    sub_list_count = len(alist) // 2

    while sub_list_count > 0:

        for start_position in range(sub_list_count):
            gapInsertionSort(alist, start_position, sub_list_count)

        print('After increments of size %s, The list is %s' % (sub_list_count, alist))

        sub_list_count = sub_list_count // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentValue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = currentValue


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    shellSort(alist)
    print(alist)

"""
[54, 26, 93, 17, 77, 31, 44, 55, 20]
After increments of size 4, The list is [20, 26, 44, 17, 54, 31, 93, 55, 77]
After increments of size 2, The list is [20, 17, 44, 26, 54, 31, 77, 55, 93]
After increments of size 1, The list is [17, 20, 26, 31, 44, 54, 55, 77, 93]
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
