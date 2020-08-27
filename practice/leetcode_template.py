# noinspection PyUnresolvedReferences
# noinspection PyUnresolvedReferences
import heapq
# noinspection PyUnresolvedReferences
import random
import unittest
# noinspection PyUnresolvedReferences
from collections import Counter
# noinspection PyUnresolvedReferences
from collections import defaultdict
# noinspection PyUnresolvedReferences
from collections import deque
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
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        for n in nums:
            if not res or n > res[-1]:
                res.append(n)
            else:
                l, r = 0, len(res) - 1
                index = r
                while l <= r:
                    m = l + (r - l) // 2
                    if res[m] >= n:
                        index = m
                        r = m - 1
                    else:
                        l = m + 1
                res[index] = n

        return len(res)


class TestSolution(unittest.TestCase):
    method = Solution().lengthOfLIS

    def test_1(self):
        self.assertEqual(self.method([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_2(self):
        pass
        # self.assertEqual(self.method([2], 3), -1)

    # def test_3(self):
    #     self.assertEqual(self.method('4193 with words'), 4193)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
