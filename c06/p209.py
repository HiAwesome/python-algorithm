from pythonds.trees.binaryTree import BinaryTree


def preorder(tree: BinaryTree):
    # 前序遍历
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def inorder(tree: BinaryTree):
    # 中序遍历
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


def postorder(tree: BinaryTree):
    # 后序遍历
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

