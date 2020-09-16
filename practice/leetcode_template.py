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


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []

        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break

            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break

        return res


class TestSolution(unittest.TestCase):
    method = Solution().spiralOrder

    def test_1(self):
        self.assertEqual(self.method([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
                         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    unittest.main()
