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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 如果间隔数小于任务数，则返回数组长度
        # 如果间隔数大于等于任务数，则计算结果：(max(相同类出现的次数)-1)*(n+1) + 相同类出现次数最多的类数量
        count = Counter(tasks)
        # 任务数
        length = len(count)

        # 相同类出现的最大次数
        all_count = count.values()
        max_cnt = max(all_count)
        # 相同类出现次数最多的类数量
        max_cnt_tasks = Counter(all_count).get(max_cnt)
        res = (max_cnt - 1) * (n + 1) + max_cnt_tasks

        return res if length < n else max(len(tasks), res)


class TestSolution(unittest.TestCase):
    method = Solution().leastInterval

    def test_1(self):
        # pass
        self.assertEqual(self.method(["A", "A", "A", "B", "B", "B"], 2), 8)

    def test_2(self):
        pass
        # self.assertEqual(self.method(2, 4), '0.5')

    def test_3(self):
        pass
        # self.assertEqual(self.method('ZY'), 701)

    # def test_4(self):
    #     self.assertEqual(self.method('words and 987'), 0)

    # def test_5(self):
    #     self.assertEqual(self.method('-91283472332'), -2147483648)


if __name__ == '__main__':
    unittest.main()
