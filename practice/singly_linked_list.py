"""
设计链表
https://leetcode-cn.com/problems/design-linked-list/

单向链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index < 0:
            index = 0

        self.size += 1
        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next

        to_add = ListNode(val)
        to_add.next = predecessor.next
        predecessor.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next

        predecessor.next = predecessor.next.next
