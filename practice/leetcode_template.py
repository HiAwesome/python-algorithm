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
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float('inf')] * (amount + 1)
        res[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                res[i] = min(res[i], res[i - coin] + 1)

        return res[-1] if res[-1] != float('inf') else -1


class TestSolution(unittest.TestCase):
    method = Solution().coinChange

    def test_1(self):
        self.assertEqual(self.method([1, 2, 5], 11), 3)

    def test_2(self):
        self.assertEqual(self.method([2], 3), -1)

    # def test_3(self):
    #     self.assertEqual(self.method('4193 with words'), 4193)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
