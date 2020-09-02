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


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        visited = set([beginWord, endWord])
        begin_visited = set([beginWord])
        end_visited = set([endWord])
        word_len = len(beginWord)
        step = 1

        while begin_visited and end_visited:
            if len(begin_visited) > len(end_visited):
                begin_visited, end_visited = end_visited, begin_visited

            next_level_visited = set()
            for word in begin_visited:
                for i in range(word_len):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + char + word[i + 1:]
                        if next_word in word_set:
                            if next_word in end_visited:
                                return step + 1
                            if next_word not in visited:
                                next_level_visited.add(next_word)
                                visited.add(next_word)

            begin_visited = next_level_visited
            step += 1
        return 0


class TestSolution(unittest.TestCase):
    method = Solution().lengthOfLongestSubstring

    def test_1(self):
        # pass
        self.assertEqual(self.method('abcabcbb'), 3)

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
