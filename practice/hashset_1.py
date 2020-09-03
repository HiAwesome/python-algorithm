"""
设计哈希集合
https://leetcode-cn.com/problems/design-hashset/
"""


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node


class Bucket:
    def __init__(self):
        self.head = Node(0, None)

    def contains(self, value):
        curr = self.head.next
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def add(self, value):
        if not self.contains(value):
            new_node = Node(value, self.head.next)
            self.head.next = new_node

    def remove(self, value):
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next


class MyHashSet(object):
    def __init__(self):
        self.key_range = 2069
        self.bucket_array = [Bucket() for _ in range(self.key_range)]

    def __get_hash_key(self, key):
        return key % self.key_range

    def add(self, key):
        self.bucket_array[self.__get_hash_key(key)].add(key)

    def remove(self, key):
        self.bucket_array[self.__get_hash_key(key)].remove(key)

    def contains(self, key):
        return self.bucket_array[self.__get_hash_key(key)].contains(key)
