"""
https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/184-ms-faster-than-6149-of-python3-by-yaosw/
"""

from collections import defaultdict


class TireNode:
    def __init__(self):
        # dict的value是TireNode对象而不是字符
        self.node = defaultdict(TireNode)
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TireNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            cur = cur.node[w]

        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w in cur.node:
                cur = cur.node[w]
            else:
                return False

        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for p in prefix:
            if p in cur.node:
                cur = cur.node[p]
            else:
                return False

        return True


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie

        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]

        # 这里的'-'就相当于前面声明的isEnd, 用来标记是不是结束了, 因为是用字典实现的所以可以随便声明key去标记
        t["-"] = True

    def search(self, word):
        t = self.trie

        for c in word:
            if c not in t: return False
            t = t[c]

        return "-" in t

    def startsWith(self, prefix):
        t = self.trie

        for c in prefix:
            if c not in t: return False
            t = t[c]

        return True
