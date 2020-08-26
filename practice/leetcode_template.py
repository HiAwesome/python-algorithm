# noinspection PyUnresolvedReferences
# noinspection PyUnresolvedReferences
import heapq
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
import random


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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return -1

        array = []
        for i in range(k):
            heapq.heappush(array, nums[i])

        for i in range(k, n):
            top = array[0]
            if nums[i] > top:
                heapq.heapreplace(array, nums[i])

        return array[0]


class TestSolution(unittest.TestCase):
    method = Solution().findKthLargest

    def test_1(self):
        self.assertEqual(self.method([3, 2, 1, 5, 6, 4], 2), 5)

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
