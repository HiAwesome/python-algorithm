"""
二叉树的三种遍历方式
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
"""
from typing import List


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历 递归
def preR(root: TreeNode) -> List[int]:
    return [root.val] + preR(root.left) + preR(root.right) if root else []


# 前序遍历 迭代
def pre(root: TreeNode) -> List[int]:
    if not root:
        return []

    stack, res = [root], []

    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


# 中序遍历 递归
def inR(root: TreeNode) -> List[int]:
    return inR(root.left) + [root.val] + inR(root.right) if root else []


# 中序遍历 迭代
def ino(root: TreeNode) -> List[int]:
    if not root:
        return []

    node, stack, res = root, [], []

    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right
    return res


# 后序遍历 递归
def postR(root: TreeNode) -> List[int]:
    return postR(root.left) + postR(root.right) + [root.val] if root else []


# 后序遍历 迭代
def post(root: TreeNode) -> List[int]:
    if not root:
        return []

    stack, res = [root], []

    while stack:
        node = stack.pop()
        if node:
            stack.append(node)
            stack.append(None)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        else:
            node = stack.pop()
            res.append(node.val)

    return res
