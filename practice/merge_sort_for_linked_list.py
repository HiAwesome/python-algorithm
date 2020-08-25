"""
链表的归并排序
https://leetcode-cn.com/problems/sort-list/
"""


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
