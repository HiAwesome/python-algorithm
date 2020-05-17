def insertionSort(alist):
    for index in range(1, len(alist)):

        currentValue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentValue


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    insertionSort(alist)
    print(alist)

"""
[54, 26, 93, 17, 77, 31, 44, 55, 20]
[17, 20, 26, 31, 44, 54, 55, 77, 93]
"""
