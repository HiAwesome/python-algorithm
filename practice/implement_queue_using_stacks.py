"""
用栈实现队列
https://leetcode-cn.com/problems/implement-queue-using-stacks/
"""


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.in_stack:
            self.front = x
        self.in_stack.append(x)

    def pop(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            self.front = None
        return self.out_stack.pop()

    def peek(self) -> int:
        return self.out_stack[-1] if self.out_stack else self.front

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
