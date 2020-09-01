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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        total = m * n
        ans = [0] * total

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        r, c = 0, 0
        di = 0

        for i in range(total):
            ans[i] = matrix[r][c]
            visited[r][c] = True
            nr, nc = r + directions[di][0], c + directions[di][1]

            if not (0 <= nr < m and 0 <= nc < n and not visited[nr][nc]):
                di = (di + 1) % 4

            r += directions[di][0]
            c += directions[di][1]

        return ans




class TestSolution(unittest.TestCase):
    method = Solution().spiralOrder

    def test_1(self):
        # pass
        self.assertEqual(self.method([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_2(self):
        pass
        # self.assertEqual(self.method([1, 0, 1, 1], 1), True)

    def test_3(self):
        pass
        # self.assertEqual(self.method([1, 2, 3, 1, 2, 3], 2), False)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
