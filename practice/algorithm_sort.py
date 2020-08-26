'''
Python 实现经典排序算法：
冒泡排序、选择排序、插入排序、希尔排序、归并排序、快速排序、堆排序
http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/

力扣练手: https://leetcode-cn.com/problems/sort-an-array/
'''
import random


# 冒泡排序
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(1, n - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums


# 选择排序
def select_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums


# 插入排序
def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            temp, index = nums[i], i
            for j in range(i - 1, -1, -1):
                if nums[j] > temp:
                    nums[j + 1], index = nums[j], j
                else:
                    break
            nums[index] = temp
    return nums


# 希尔排序
def shell_sort(nums):
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2
    return nums


# 归并排序
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    l = merge_sort(nums[:mid])
    r = merge_sort(nums[mid:])
    return merge(l, r)


def merge(l, r):
    li, ri = 0, 0
    res = []
    while li < len(l) and ri < len(r):
        if l[li] < r[ri]:
            res.append(l[li])
            li += 1
        else:
            res.append(r[ri])
            ri += 1
    res += l[li:]
    res += r[ri:]
    return res


# 快速排序
def quick_sort(nums):
    return qsort(nums, 0, len(nums) - 1)


def qsort(nums, l, r):
    if l >= r:
        return nums
    # 随机化切分元素，避免递归树退化为链表
    random_index = random.randint(l, r)
    nums[random_index], nums[l] = nums[l], nums[random_index]

    key = nums[l]
    li = l
    ri = r
    while li < ri:
        while li < ri and nums[ri] >= key:
            ri -= 1
        while li < ri and nums[li] <= key:
            li += 1
        nums[li], nums[ri] = nums[ri], nums[li]

    nums[l], nums[ri] = nums[ri], nums[l]
    qsort(nums, l, li - 1)
    qsort(nums, ri + 1, r)
    return nums


# 堆排序
def heap_sort(nums):
    n = len(nums)
    first = n // 2 - 1
    for start in range(first, -1, -1):
        max_heapify(nums, start, n - 1)
    for end in range(n - 1, 0, -1):
        nums[end], nums[0] = nums[0], nums[end]
        max_heapify(nums, 0, end - 1)
    return nums


def max_heapify(nums, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and nums[child] < nums[child + 1]:
            child = child + 1
        if nums[root] < nums[child]:
            nums[root], nums[child] = nums[child], nums[root]
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
