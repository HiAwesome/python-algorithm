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
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        res = []

        if (numerator > 0) ^ (denominator > 0):
            res.append('-')

        numerator, denominator = abs(numerator), abs(denominator)
        a, b = divmod(numerator, denominator)
        res.append(str(a))

        if b == 0:
            return ''.join(res)
        else:
            res.append('.')

        loc = {b: len(res)}

        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            if b in loc:
                res.insert(loc[b], '(')
                res.append(')')
                break
            loc[b] = len(res)

        return ''.join(res)


class TestSolution(unittest.TestCase):
    method = Solution().fractionToDecimal

    def test_1(self):
        self.assertEqual(self.method(2, 3), '0.(6)')

    def test_2(self):
        # pass
        self.assertEqual(self.method(2, 4), '0.5')

    def test_3(self):
        pass
        # self.assertEqual(self.method('ZY'), 701)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
