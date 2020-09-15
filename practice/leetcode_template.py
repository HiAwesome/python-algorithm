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
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0

        if n < 0:
            n = -n
            x = 1 / x

        res = 1

        while n:
            if n % 2 != 0:
                res *= x
            x *= x
            n //= 2

        return res


class TestSolution(unittest.TestCase):
    method = Solution().myPow

    def test_1(self):
        self.assertEqual(self.method(2.0, 10), 1024.0)

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
