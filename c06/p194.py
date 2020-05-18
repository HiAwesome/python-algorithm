def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == '__main__':
    r = BinaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertRight(r, 6)
    insertRight(r, 7)
    print(r)

    child = getLeftChild(r)
    print(child)
    setRootVal(child, 9)
    print(r)
    insertLeft(child, 11)
    print(r)
    print(getRightChild(getRightChild(r)))

"""
[3, [5, [4, [], []], []], [7, [], [6, [], []]]]
[5, [4, [], []], []]
[3, [9, [4, [], []], []], [7, [], [6, [], []]]]
[3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
[6, [], []]
"""
