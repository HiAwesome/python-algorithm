myTree = [
    'a',  # root
    ['b',  # left subtree
     ['d', [], []],
     ['e', [], []]
     ],
    ['c',  # right subtree
     ['f', [], []],
     []]
]

if __name__ == '__main__':
    print(myTree)
    print('left subtree = %s' % myTree[1])
    print('root = %s' % myTree[0])
    print('right subtree = %s' % myTree[2])

"""
['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]
left subtree = ['b', ['d', [], []], ['e', [], []]]
root = a
right subtree = ['c', ['f', [], []], []]
"""
