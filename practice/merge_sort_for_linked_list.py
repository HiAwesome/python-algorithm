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
            return

        def merge(leftIndex, rightIndex):
            if leftIndex == rightIndex:
                return lists[leftIndex]
            mid = leftIndex + (rightIndex - leftIndex) // 2
            left = merge(leftIndex, mid)
            right = merge(mid + 1, rightIndex)
            return mergeTwoList(left, right)

        def mergeTwoList(left, right):
            dummy = index = ListNode(0)

            while left and right:
                if left.val <= right.val:
                    index.next = left
                    left = left.next
                else:
                    index.next = right
                    right = right.next
                index = index.next

            index.next = left if left else right
            return dummy.next

        n = len(lists)
        return merge(0, n - 1)
