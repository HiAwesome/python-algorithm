class Deque:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    d = Deque()
    print(d, d.isEmpty())

    d.addRear(4)
    print(d)

    d.addRear('dog')
    print(d)

    d.addFront('cat')
    print(d)

    d.addFront(True)
    print(d, d.size(), d.isEmpty())

    d.addRear(8.4)
    print(d)

    e1 = d.removeRear()
    print(e1, d)

    e2 = d.removeFront()
    print(e2, d)

"""
[] True
[4]
['dog', 4]
['dog', 4, 'cat']
['dog', 4, 'cat', True] 4 False
[8.4, 'dog', 4, 'cat', True]
8.4 ['dog', 4, 'cat', True]
True ['dog', 4, 'cat']
"""
