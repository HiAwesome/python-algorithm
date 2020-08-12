"""
https://leetcode-cn.com/problems/min-stack/solution/zui-xiao-zhan-by-leetcode-solution/
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        容量永远相等，同增同减
        """
        self.data_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.data_stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1] if self.min_stack else x))

    def pop(self) -> None:
        self.data_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.data_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
