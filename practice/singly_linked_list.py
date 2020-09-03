"""
设计链表
https://leetcode-cn.com/problems/design-linked-list/

单向链表
"""


class Node:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        node = self.head
        for _ in range(index + 1):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index < 0:
            index = 0

        prev = self.head
        for _ in range(index):
            prev = prev.next

        self.size += 1
        to_add = Node(val)
        to_add.next = prev.next
        prev.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        self.size -= 1
        prev.next = prev.next.next
