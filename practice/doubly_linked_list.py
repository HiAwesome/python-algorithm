"""
https://leetcode-cn.com/problems/design-linked-list/solution/she-ji-lian-biao-by-leetcode/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        # 创建伪头和伪尾节点
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        获取链表中第index个节点的值。如果索引无效，则返回-1。
        """
        # 如果索引无效
        if index < 0 or index >= self.size:
            return -1

        # 通过比较 index 和 size - index 的大小判断从头开始较快还是从尾巴开始较快。
        # 从较快的方向开始。
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        在链接列表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
        """
        predecessor, successor = self.head, self.head.next

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = predecessor
        to_add.next = successor
        predecessor.next = to_add
        successor.prev = to_add

    def addAtTail(self, val: int) -> None:
        """
        将值val的节点追加到链接列表的最后一个元素。
        """
        successor, predecessor = self.tail, self.tail.prev

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = predecessor
        to_add.next = successor
        predecessor.next = to_add
        successor.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        """
        在链接列表的第index个节点之前添加一个值为val的节点。
        如果index等于链表的长度，则该节点将附加到链表的末尾。
        如果index大于长度，则不会插入该节点。
        """
        # 如果index大于长度，则不会插入该节点。
        if index > self.size:
            return

        # [太奇怪了]如果index为负，则该节点将插入列表的开头。
        if index < 0:
            index = 0

        # 查找要添加的节点的前继节点和后继节点
        if index < self.size - index:
            predecessor = self.head
            for _ in range(index):
                predecessor = predecessor.next
            successor = predecessor.next
        else:
            successor = self.tail
            for _ in range(self.size - index):
                successor = successor.prev
            predecessor = successor.prev

        # 执行插入操作
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = predecessor
        to_add.next = successor
        predecessor.next = to_add
        successor.prev = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        如果索引有效，请删除链接列表中的第index个节点。
        """
        # 如果索引无效什么也不做
        if index < 0 or index >= self.size:
            return

        # 查找要删除的节点的前继节点和后继节点
        if index < self.size - index:
            predecessor = self.head
            for _ in range(index):
                predecessor = predecessor.next
            successor = predecessor.next.next
        else:
            successor = self.tail
            for _ in range(self.size - index - 1):
                successor = successor.prev
            predecessor = successor.prev.prev

        # 执行删除操作
        self.size -= 1
        predecessor.next = successor
        successor.prev = predecessor
