"""
https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/yong-zhan-shi-xian-dui-lie-by-leetcode/
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
        if self.out_stack:
            return self.out_stack[-1]
        else:
            return self.front

    def empty(self) -> bool:
        if not self.in_stack and not self.out_stack:
            return True
        else:
            return False
