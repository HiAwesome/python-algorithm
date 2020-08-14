"""
https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/er-cha-sou-suo-shu-die-dai-qi-by-leetcode/
"""

# 中序遍历，初始化时完成遍历，空间复杂度 O(n)
class BSTIteratorA:

    def __init__(self, root: TreeNode):
        self.node_array = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        self.node_array.append(node.val)
        self._inorder(node.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.node_array[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.node_array)

# 中序遍历，受控递归，next 方法时不断更新元素，空间复杂度 O(h)
class BSTIteratorB:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

