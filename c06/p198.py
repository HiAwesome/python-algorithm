class BinaryTree:
    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            # 第二种情况的特征在于具有现有左孩子的节点。在第二种情况下，我们插入一个节点并将现有的子节点放到树中的下一个层。
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.root = obj

    def getRootVal(self):
        return self.root

    def __str__(self):
        return str(self.root)


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())

    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())

    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())

    r.getRightChild().setRootVal('Hello')
    print(r.getRightChild().getRootVal())

"""
a
None
b
b
c
c
Hello
"""
