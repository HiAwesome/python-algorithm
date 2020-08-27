"""
二叉树的序列化与反序列化
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/

代码参考：
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/solution/shou-hui-tu-jie-gei-chu-dfshe-bfsliang-chong-jie-f/447052
"""
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if not root:
            return []

        q = deque()
        q.append(root)
        res = ''

        while q:
            node = q.popleft()
            if node:
                res += str(node.val) + ','
                q.append(node.left)
                q.append(node.right)
            else:
                res += 'X,'

        return res

    def deserialize(self, data):
        if not data:
            return None

        data_q = deque(data.split(','))
        root = TreeNode(data_q.popleft())
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if data_q:
                val = data_q.popleft()
                if val != 'X':
                    node.left = TreeNode(val)
                    q.append(node.left)
            if data_q:
                val = data_q.popleft()
                if val != 'X':
                    node.right = TreeNode(val)
                    q.append(node.right)

        return root
