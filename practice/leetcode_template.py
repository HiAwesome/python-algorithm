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


from collections import defaultdict


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def lpow(o1, o2):
            l1 = o1[0] - o2[0]
            l2 = o1[1] - o2[1]
            # 不开根号，避免小数精度问题
            return l1 * l1 + l2 * l2

        array = [p1, p2, p3, p4]
        n = len(array)
        dic = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                distance = lpow(array[i], array[j])
                dic[distance] += 1

        if len(dic) != 2:
            return False

        dic = {v: k for k, v in dic.items()}

        keys = dic.keys()
        if 2 not in keys or 4 not in keys:
            return False

        short_dis, long_dis = dic[4], dic[2]

        if short_dis * 2 == long_dis:
            return True
        else:
            return False


class TestSolution(unittest.TestCase):
    method = Solution().validSquare

    def test_1(self):
        self.assertEqual(self.method([0, 0], [1, 1], [1, 0], [0, 1]), True)

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
