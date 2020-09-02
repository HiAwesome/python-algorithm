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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []

        for index, value in enumerate(nums):
            if d and d[0] <= index - k:
                d.popleft()
            while d and value > nums[d[-1]]:
                d.pop()
            d.append(index)

            if index >= k - 1:
                res.append(nums[d[0]])

        return res


class TestSolution(unittest.TestCase):
    method = Solution().maxSlidingWindow

    def test_1(self):
        # pass
        self.assertEqual(self.method([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])

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
