"""
设计循环队列
https://leetcode-cn.com/problems/design-circular-queue/
"""


class MyCircularQueue:

    def __init__(self, capacity: int):
        self.queue = [0] * capacity
        self.headIndex = 0
        self.size = 0
        self.capacity = capacity

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.queue[(self.headIndex + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[(self.headIndex + self.size - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
