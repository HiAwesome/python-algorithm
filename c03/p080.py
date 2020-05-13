class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop() if not self.is_empty() else 'The stack is empty now!'

    def peek(self):
        return self.items[-1] if not self.is_empty() else 'The stack is empty now!'

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    print(s.pop())

    s.push(4)
    print(s)

    s.push('dog')
    print(s)
    print(s.peek())

    s.push(True)
    print(s)
    print(s.size())
    print(s.is_empty())

    s.push(8.4)
    print(s)

    e1 = s.pop()
    print(e1)
    print(s)

    e2 = s.pop()
    print(e2)
    print(s)
    print(s.size())
