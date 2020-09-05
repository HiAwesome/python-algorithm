"""
LFU Cache
https://leetcode-cn.com/problems/lfu-cache/

实现
https://leetcode-cn.com/problems/lfu-cache/solution/lfuhuan-cun-by-leetcode-solution/
"""

from collections import defaultdict


class Node:
    def __init__(self, key=None, value=None, prev=None, next=None, count=0):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        self.count = count

    def insert(self, next):
        next.prev = self
        next.next = self.next
        self.next.prev = next
        self.next = next


def create_linked_list():
    head = Node()
    tail = Node()
    head.next = tail
    tail.prev = head
    return (head, tail)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.freqMap = defaultdict(create_linked_list)
        self.keyMap = {}

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
            if node.prev is self.freqMap[node.count][0] and node.next is self.freqMap[node.count][-1]:
                self.freqMap.pop(node.count)
        return node.key

    def increase(self, node):
        node.count += 1
        self.delete(node)
        self.freqMap[node.count][-1].prev.insert(node)
        if node.count == 1:
            self.minFreq = 1
        elif self.minFreq == node.count - 1:
            head, tail = self.freqMap[node.count - 1]
            if head.next is tail:
                self.minFreq = node.count

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.value = value
            else:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].next)
                self.keyMap.pop(deleted)
            self.increase(node)
