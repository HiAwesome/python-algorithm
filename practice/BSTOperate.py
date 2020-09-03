"""
二叉搜索树的搜索，插入，删除
https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
https://leetcode-cn.com/problems/delete-node-in-a-bst/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# noinspection PyTypeChecker
class Solution:
    # 递归搜索
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or val == root.val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    # 迭代搜索
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root

    # 递归插入
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

    # 迭代插入
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        new_node = TreeNode(val)

        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    return root
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    return root

        return new_node

    # 递归删除
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
