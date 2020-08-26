# noinspection PyUnresolvedReferences
# noinspection PyUnresolvedReferences
import heapq
import re
import unittest
# noinspection PyUnresolvedReferences
from collections import Counter
# noinspection PyUnresolvedReferences
from collections import defaultdict
# noinspection PyUnresolvedReferences
from collections import deque
# noinspection PyUnresolvedReferences
from random import shuffle
# noinspection PyUnresolvedReferences
from typing import List
# noinspection PyUnresolvedReferences
import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k_index = n - k
        l, r = 0, n - 1

        # 将 value 放在排序后合适的 index 上
        def partition(l, r):
            # 随机化切分元素, 避免递归树退化为链表
            random_index = random.randint(l, r)
            nums[random_index], nums[l] = nums[l], nums[random_index]
            value = nums[l]
            index = l
            for i in range(l + 1, r + 1):
                if nums[i] < value:
                    index += 1
                    nums[i], nums[index] = nums[index], nums[i]

            nums[l], nums[index] = nums[index], nums[l]
            return index

        while True:
            index = partition(l, r)
            if index == k_index:
                return nums[index]
            elif index < k_index:
                l = index + 1
            else:
                r = index - 1


class TestSolution(unittest.TestCase):
    method = Solution().findKthLargest

    def test_1(self):
        self.assertEqual(self.method([3, 2, 1, 5, 6, 4], 2), 5)

    # def test_2(self):
    #     self.assertEqual(self.method(["dog","racecar","car"]), "")

    # def test_3(self):
    #     self.assertEqual(self.method('4193 with words'), 4193)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
