"""
设计链表
https://leetcode-cn.com/problems/design-linked-list/

双向链表
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addNode(self, predecessor, successor, val):
        self.size += 1
        to_add = Node(val)
        to_add.prev = predecessor
        to_add.next = successor
        predecessor.next = to_add
        successor.prev = to_add

    def addAtHead(self, val: int) -> None:
        self.addNode(self.head, self.head.next, val)

    def addAtTail(self, val: int) -> None:
        self.addNode(self.tail.prev, self.tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index < 0:
            index = 0

        if index < self.size - index:
            predecessor = self.head
            for _ in range(index):
                predecessor = predecessor.next
            successor = predecessor.next
        else:
            successor = self.tail
            for _ in range(self.size - index):
                successor = successor.prev
            predecessor = successor.prev

        self.addNode(predecessor, successor, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            predecessor = self.head
            for _ in range(index):
                predecessor = predecessor.next
            successor = predecessor.next.next
        else:
            successor = self.tail
            for _ in range(self.size - index - 1):
                successor = successor.prev
            predecessor = successor.prev.prev

        self.size -= 1
        predecessor.next = successor
        successor.prev = predecessor
