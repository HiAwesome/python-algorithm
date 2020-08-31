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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        first_index = 0
        n = len(nums)

        for first_index in range(n - 2):
            if nums[first_index] > 0:
                break

            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue

            l, r = first_index + 1, n - 1
            while l < r:
                s = nums[first_index] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    res.append([nums[first_index], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res



class TestSolution(unittest.TestCase):
    method = Solution().threeSum

    def test_1(self):
        # pass
        self.assertEqual(self.method([-1, 0, 1, 2, -1, -4]), [
            [-1, -1, 2],
            [-1, 0, 1]
        ])

    def test_2(self):
        pass
        # self.assertEqual(self.method('a', 'b'), False)

    def test_3(self):
        pass
        # self.assertEqual(self.method('ZY'), 701)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
