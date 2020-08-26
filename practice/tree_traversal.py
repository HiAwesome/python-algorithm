"""
二叉树的三种遍历方式
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

方法解析，完全模仿系统栈操作
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/mo-fang-di-gui-zhi-bian-yi-xing-by-sonp/417844
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

        if not node:
            node = stack.pop()
            res.append(node.val)
        else:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            stack.append(node)
            stack.append(None)

    return res


# 中序遍历 递归
def inR(root: TreeNode) -> List[int]:
    return inR(root.left) + [root.val] + inR(root.right) if root else []


# 中序遍历 迭代
def ino(root: TreeNode) -> List[int]:
    if not root:
        return []

    stack, res = [root], []

    while stack:
        node = stack.pop()

        if not node:
            node = stack.pop()
            res.append(node.val)
        else:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            stack.append(None)
            if node.left:
                stack.append(node.left)

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

        if not node:
            node = stack.pop()
            res.append(node.val)
        else:
            stack.append(node)
            stack.append(None)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return res
