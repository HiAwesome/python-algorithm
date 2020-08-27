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
    def titleToNumber(self, s: str) -> int:
        res = 0

        for c in s:
            res *= 26
            res += ord(c) - ord('A') + 1

        return res


class TestSolution(unittest.TestCase):
    method = Solution().titleToNumber

    def test_1(self):
        self.assertEqual(self.method('A'), 1)

    def test_2(self):
        self.assertEqual(self.method('AB'), 28)

    def test_3(self):
        self.assertEqual(self.method('ZY'), 701)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
