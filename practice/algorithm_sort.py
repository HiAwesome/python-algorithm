'''
Python 实现经典排序算法：
冒泡排序、选择排序、插入排序、希尔排序、归并排序、快速排序、堆排序
http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/
'''


# 冒泡排序
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(1, n - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


# 选择排序
def select_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


# 插入排序
def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        if array[i] < array[i - 1]:
            temp, index = array[i], i
            for j in range(i - 1, -1, -1):
                if array[j] > temp:
                    array[j + 1], index = array[j], j
                else:
                    break
            array[index] = temp
    return array


# 希尔排序
def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array


# 归并排序
def merge_sort(array):
    if len(array) <= 1:
        return array
    num = len(array) // 2
    left = merge_sort(array[:num])
    right = merge_sort(array[num:])
    return merge(left, right)


def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result


# 快速排序
def quick_sort(array):
    return qsort(array, 0, len(array) - 1)


def qsort(array, left, right):
    if left >= right:
        return array
    key = array[left]
    lp = left
    rp = right
    while lp < rp:
        while array[rp] >= key and lp < rp:
            rp -= 1
        while array[lp] <= key and lp < rp:
            lp += 1
        array[lp], array[rp] = array[rp], array[lp]

    array[left], array[rp] = array[rp], array[left]
    qsort(array, left, lp - 1)
    qsort(array, rp + 1, right)
    return array


# 堆排序
def heap_sort(array):
    n = len(array)
    first = n // 2 - 1
    for start in range(first, -1, -1):
        max_heapify(array, start, n - 1)
    for end in range(n - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        max_heapify(array, 0, end - 1)
    return array


def max_heapify(array, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child + 1]:
            child = child + 1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


if __name__ == '__main__':
    array = [6, 5, 4, 3, 2, 1]

    print(bubble_sort(array))

    print(select_sort(array))

    print(insert_sort(array))

    print(shell_sort(array))

    print(merge_sort(array))

    print(quick_sort(array))

    print(heap_sort(array))
