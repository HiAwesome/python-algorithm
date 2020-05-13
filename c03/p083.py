class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() if not self.isEmpty() else 'The Queue is empty now!'

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    print(q, q.isEmpty())

    q.enqueue(4)
    print(q)

    q.enqueue('dog')
    print(q)

    q.enqueue(True)
    print(q, q.size(), q.isEmpty())

    q.enqueue(8.4)
    print(q)

    e1 = q.dequeue()
    print(e1, q)

    e2 = q.dequeue()
    print(e2, q, q.size())

"""
[] True
[4]
['dog', 4]
[True, 'dog', 4] 3 False
[8.4, True, 'dog', 4]
4 [8.4, True, 'dog']
dog [8.4, True] 2
"""
