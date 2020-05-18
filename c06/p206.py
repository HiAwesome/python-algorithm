import operator

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ('+', '-', '*', '/', ')'):
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ('+', '-', '*', '/'):
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

    return eTree


def evaluate(parseTree: BinaryTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


def postorder_evaluate(tree: BinaryTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    if tree:
        res1 = postorder_evaluate(tree.getLeftChild())
        res2 = postorder_evaluate(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


def print_exp(tree: BinaryTree):
    # 优化后的方法，去掉每个数字的左右括号
    sVal = ''

    if tree:
        str_val = str(tree.getRootVal())
        result = print_exp(tree.getLeftChild()) + str_val + print_exp(tree.getRightChild())

        if str_val.isnumeric():
            sVal = result
        else:
            sVal = '(' + result + ')'

    return sVal


if __name__ == '__main__':
    # 需要空格夹杂以备切割，如果去掉此操作则多位数解析为多个单位数，会出错
    pt = buildParseTree('( ( 10 + 5 ) * 3 )')
    pt.postorder()

    print()
    print('result is %d' % evaluate(pt))

    print()
    print('用后序遍历的方法计算结果： %d' % postorder_evaluate(pt))

    print()
    print('用中序遍历的方法打印表达式： %s' % print_exp(pt))

"""
10
5
+
3
*

result is 45

用后序遍历的方法计算结果： 45

用中序遍历的方法打印表达式： ((10+5)*3)
"""
