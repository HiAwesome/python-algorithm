from collections import deque
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder_before = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= inorder_before:
                return False

            inorder_before = root.val
            root = root.right

        return True



if __name__ == '__main__':
    s = Solution()
    print(s.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
