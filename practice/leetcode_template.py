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
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = (s + s)
        n = len(s)
        find = s2.find(s, 1)
        return find != n


class TestSolution(unittest.TestCase):
    method = Solution().repeatedSubstringPattern

    def test_1(self):
        self.assertEqual(self.method('aba'), False)

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
