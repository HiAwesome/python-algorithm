"""
LRU Cache
https://leetcode-cn.com/problems/lru-cache/

实现
https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/
"""


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __split_node(self, key):
        node = self.dic[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def __move_to_end(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.dic:
            self.__move_to_end(self.__split_node(key))
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].value = value
            self.__move_to_end(self.__split_node(key))
        else:
            if len(self.dic) == self.capacity:
                self.dic.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            node = Node(key, value)
            self.dic[key] = node
            self.__move_to_end(node)
