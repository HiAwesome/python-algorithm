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
from random import shuffle
# noinspection PyUnresolvedReferences
from typing import List
# noinspection PyUnresolvedReferences
from pprint import pprint


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
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        pprint(dp)

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        pprint(dp)
        return dp[-1][-1]


class TestSolution(unittest.TestCase):
    method = Solution().uniquePaths

    def test_1(self):
        self.assertEqual(self.method(3, 2), 3)

    def test_2(self):
        self.assertEqual(self.method(7, 3), 28)

    # def test_3(self):
    #     self.assertEqual(self.method('4193 with words'), 4193)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
