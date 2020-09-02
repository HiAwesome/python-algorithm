"""
链表的归并排序
https://leetcode-cn.com/problems/sort-list/
合并K个升序链表
https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        dummy = res = ListNode(0)

        while left and right:

            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next

            dummy = dummy.next

        dummy.next = left if left else right
        return res.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return ListNode(0)

        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoList(l1, l2)

    def mergeTwoList(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        node = ListNode(0)
        h = node

        while l1 and l2:
            if l1.val <= l2.val:
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next

        h.next = l1 if l1 else l2
        return node.next
