# noinspection PyUnresolvedReferences
import collections
# noinspection PyUnresolvedReferences
import heapq
# noinspection PyUnresolvedReferences
import random
# noinspection PyUnresolvedReferences
import unittest
# noinspection PyUnresolvedReferences
from pprint import pprint
# noinspection PyUnresolvedReferences
from random import shuffle
# noinspection PyUnresolvedReferences
from typing import List


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
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = cur_min = cur_max = nums[0]

        for num in nums[1:]:
            cur_max *= num
            cur_min *= num
            cur_max, cur_min = max(cur_max, cur_min, num), min(cur_max, cur_min, num)
            res = max(res, cur_max)

        return res


class TestSolution(unittest.TestCase):
    method = Solution().maxProduct

    def test_1(self):
        # pass
        self.assertEqual(self.method([-1, -2, -9, -6]), 108)

    # def test_2(self):
    #     pass
    # self.assertEqual(self.method([1, 0, 1, 1], 1), True)

    # def test_3(self):
    #     pass
    # self.assertEqual(self.method([1, 2, 3, 1, 2, 3], 2), False)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
