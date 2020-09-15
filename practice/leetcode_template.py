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
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        dp_c = [1] * n
        max_v = 0

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        dp_c[i] = dp_c[j]
                    elif dp[j] + 1 == dp[i]:
                        dp_c[i] += dp_c[j]
            max_v = max(max_v, dp[i])

        ans = 0
        for i in range(n - 1, -1, -1):
            if dp[i] == max_v:
                ans += dp_c[i]

        return ans

        mdp = max(dp)
        return dp.count(mdp)


class TestSolution(unittest.TestCase):
    method = Solution().findNumberOfLIS

    def test_1(self):
        self.assertEqual(self.method([1, 3, 5, 4, 7]), 2)

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
