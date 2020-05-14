"""
汉诺塔问题
"""


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fromPole, toPole):
    print('moving disk from %s to %s' % (fromPole, toPole))


if __name__ == '__main__':
    moveTower(3, 'A', 'B', 'C')
