"""
https://leetcode-cn.com/problems/design-linked-list/solution/she-ji-lian-biao-by-leetcode/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        # 创建伪头节点
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """
        获取链表中第index个节点的值。如果索引无效，则返回-1。
        """
        # 如果索引无效
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        # 从前哨节点移动到所需索引所需的索引步骤
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        在链接列表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        将值val的节点追加到链接列表的最后一个元素。
        """
        self.addAtIndex(self.size, val)

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

        self.size += 1
        # 查找要添加的节点的前继节点
        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next

        # 要添加的节点
        to_add = ListNode(val)
        # 执行插入操作
        to_add.next = predecessor.next
        predecessor.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        如果索引有效，请删除链接列表中的第index个节点。
        """
        # 如果索引无效什么也不做
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        # 查找要删除的节点的前继节点
        predecessor = self.head
        for _ in range(index):
            predecessor = predecessor.next

        # 执行删除操作
        predecessor.next = predecessor.next.next
