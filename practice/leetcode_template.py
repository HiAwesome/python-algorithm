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
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = collections.defaultdict(int)
        start, end, max_len, counter = 0, 0, 0, 0

        while end < len(s):
            if dic[s[end]] > 0:
                counter += 1
            dic[s[end]] += 1
            end += 1

            while counter > 0:
                if dic[s[start]] > 1:
                    counter -= 1
                dic[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start)

        return max_len


class TestSolution(unittest.TestCase):
    method = Solution().lengthOfLongestSubstring

    def test_1(self):
        # pass
        self.assertEqual(self.method('abcabcbb'), 3)

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
