"""
设计哈希集合
https://leetcode-cn.com/problems/design-hashset/
"""


class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None


class Bucket:
    def __init__(self):
        self.head = Node()

    def contains(self, key):
        curr = self.head.next
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False

    def add(self, key):
        if not self.contains(key):
            node = Node(key)
            node.next = self.head.next
            self.head.next = node

    def remove(self, key):
        if self.contains(key):
            prev, curr = self.head, self.head.next

            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return

                prev = curr
                curr = curr.next


class MyHashSet(object):
    def __init__(self):
        self.key_range = 2069
        self.hashset = [Bucket() for _ in range(self.key_range)]

    def __get_hash_key(self, key):
        return key % self.key_range

    def add(self, key):
        self.hashset[self.__get_hash_key(key)].add(key)

    def remove(self, key):
        self.hashset[self.__get_hash_key(key)].remove(key)

    def contains(self, key):
        return self.hashset[self.__get_hash_key(key)].contains(key)
