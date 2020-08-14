"""
https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/er-cha-sou-suo-shu-die-dai-qi-by-leetcode/
"""


class BSTIterator:

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
