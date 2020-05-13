from pythonds.basic.deque import Deque


def palchecker(a_string):
    chardeque = Deque()

    for ch in a_string:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == '__main__':
    a = 'lsdkjfskf'
    print(a, palchecker(a))

    b = 'tommot'
    print(b, palchecker(b))

"""
lsdkjfskf False
tommot True
"""
