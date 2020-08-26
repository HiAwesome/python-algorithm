# noinspection PyUnresolvedReferences
import re
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
import heapq


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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i in nums:
            map[i] = map.get(i, 0) + 1

        max_time = max(map.values())
        tongList = [[] for _ in range(max_time + 1)]

        for key, value in map.items():
            tongList[value].append(key)

        res = []

        for i in range(max_time, 0, -1):
            if tongList[i]:
                res.extend(tongList[i])
            if len(res) >= k:
                return res[:k]


class TestSolution(unittest.TestCase):
    method = Solution().topKFrequent

    def test_1(self):
        self.assertEqual(self.method([1], 1), [1])

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
