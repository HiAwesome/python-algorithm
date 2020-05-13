class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next: Node = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head: Node = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current, count = self.head, 0
        while current:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current, found = self.head, False
        while current and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current, previous, found = self.head, None, False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not previous:
            """
            如果要移除的那个元素恰好是列表中的第一个，那么 current 会引用链表的第一个节点。
            这也就意味着 previous 的引用会是 None。我们之前提到过，previous 要指向那个引用要发生变化的节点。
            在这种情况下，需要改动的不是 previous，而是链表的头节点。
            """
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())


if __name__ == '__main__':
    temp = Node(93)
    print(temp.getData())
