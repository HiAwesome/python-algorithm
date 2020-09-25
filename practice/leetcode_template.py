# noinspection PyUnresolvedReferences
import collections
# noinspection PyUnresolvedReferences
import heapq
# noinspection PyUnresolvedReferences
import random
# noinspection PyUnresolvedReferences
from pprint import pprint
# noinspection PyUnresolvedReferences
from random import shuffle
# noinspection PyUnresolvedReferences
from typing import List


class Solution:
    def remove_data(self, s) -> str:
        if not s:
            return s

        res = []
        if s[0].isalnum():
            res.append(s[0])

        for i in range(1, len(s)):
            if not s[i - 1].isalnum() and s[i].isalpha():
                res.append(s[i].upper())
            elif s[i].isalpha():
                res.append(s[i].lower())
            elif s[i].isnumeric():
                res.append(s[i])

        # 对全文首字母应用规则二
        return ''.join(res if res[0].islower() else [res[0].lower()] + res[1:])


if __name__ == '__main__':
    method = Solution().remove_data

    assert method('@WelCome to ## byteDance-2020') == 'welcomeToBytedance2020'
    assert method('WelCome to ## byteDance-2020') == 'welcomeToBytedance2020'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
