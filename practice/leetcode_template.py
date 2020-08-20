import unittest
# noinspection PyUnresolvedReferences
import re
# noinspection PyUnresolvedReferences
import collections
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
    def myAtoi(self, s: str) -> int:
        int_max, int_min = 2147483648, -2147483648
        s = s.lstrip()
        num_re = re.compile(r'^[+\-]?\d+')
        num = num_re.findall(s)
        num = int(*num)
        return max(min(num, int_max), int_min)


class TestSolution(unittest.TestCase):
    method = Solution().myAtoi

    def test_1(self):
        self.assertEqual(self.method('42'), 42)

    def test_2(self):
        self.assertEqual(self.method('   -42'), -42)

    def test_3(self):
        self.assertEqual(self.method('4193 with words'), 4193)

    def test_4(self):
        self.assertEqual(self.method('words and 987'), 0)

    def test_5(self):
        self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
