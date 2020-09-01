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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, ans = [0] * n, [0] * n, [0] * n

        L[0] = 1
        for i in range(1, n):
            L[i] = nums[i - 1] * L[i - 1]

        R[n - 1] = 1
        # for i in reversed(range(n - 1)):
        #     R[i] = nums[i + 1] * R[i + 1]
        for i in range(n - 2, -1, -1):
            R[i] = nums[i + 1] * R[i + 1]

        for i in range(n):
            ans[i] = L[i] * R[i]

        return ans


class TestSolution(unittest.TestCase):
    method = Solution().productExceptSelf

    def test_1(self):
        # pass
        self.assertEqual(self.method([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_2(self):
        pass
        # self.assertEqual(self.method([1, 0, 1, 1], 1), True)

    def test_3(self):
        pass
        # self.assertEqual(self.method([1, 2, 3, 1, 2, 3], 2), False)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
