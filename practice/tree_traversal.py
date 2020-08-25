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
        cur = stack.pop()
        res.append(cur.val)
        # 顺序：先添加右节点，再添加左节点
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return res


# 中序遍历 递归
def inR(root: TreeNode) -> List[int]:
    return inR(root.left) + [root.val] + inR(root.right) if root else []


# 中序遍历 迭代
def ino(root: TreeNode) -> List[int]:
    if not root:
        return []

    cur, stack, res = root, [], []

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
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
        cur = stack.pop()
        if cur:
            stack.append(cur)
            stack.append(None)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        else:
            cur = stack.pop()
            res.append(cur.val)

    return res
