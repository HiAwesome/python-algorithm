from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()

        n1 = len(nums1)
        n2 = len(nums2)
        i1, i2 = 0, 0
        res = []

        while i1 < n1 and i2 < n2:
            if nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                res.append(nums1[i1])
                i1 += 1
                i2 += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
