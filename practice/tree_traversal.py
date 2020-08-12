class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历 递归
def preorderTraversalRecursion(root: TreeNode) -> List[int]:
    if not root:
        return []
    return [root.val] + preorderTraversalRecursion(root.left) + preorderTraversalRecursion(root.right)


# 前序遍历 迭代
def inorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []

    stack, res = [root], []

    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return res


# 中序遍历 递归
def inorderTraversalRecursion(root: TreeNode) -> List[int]:
    if not root:
        return []
    return inorderTraversalRecursion(root.left) + [root.val] + inorderTraversalRecursion(root.right)


# 中序遍历 迭代
def inorderTraversal(root: TreeNode) -> List[int]:
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
def postorderTraversalRecursion(root: TreeNode) -> List[int]:
    if not root:
        return []
    return postorderTraversalRecursion(root.left) + postorderTraversalRecursion(root.right) + [root.val]


# 后序遍历 迭代
def inorderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []

    stack, res = [root], []

    while stack:
        cur = stack.pop()
        if not cur:
            cur = stack.pop()
            res.append(cur.val)
        else:
            stack.append(cur)
            stack.append(None)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    return res
