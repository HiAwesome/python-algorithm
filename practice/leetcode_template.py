# noinspection PyUnresolvedReferences
import re
import unittest
# noinspection PyUnresolvedReferences
from collections import defaultdict
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
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def helper(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start = end = 0
        for i in range(n):
            l1, r1 = helper(i, i)
            if r1 - l1 > end - start:
                start, end = l1, r1

            l2, r2 = helper(i, i + 1)
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end - 1]




class TestSolution(unittest.TestCase):
    method = Solution().longestPalindrome

    def test_1(self):
        self.assertEqual(self.method('ababa'), 'aba')

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
