# noinspection PyUnresolvedReferences
import re
import unittest
# noinspection PyUnresolvedReferences
from collections import deque
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
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        n = len(piles)

        l, r = 0, n - 1
        res = 0

        while l < r:
            res += piles[r - 1]
            l += 1
            r -= 2

        return res



class TestSolution(unittest.TestCase):
    method = Solution().maxCoins

    def test_1(self):
        self.assertEqual(self.method([2, 4, 1, 2, 7, 8]), 9)

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
