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


from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sorted_set = SortedSet()

        for i in range(len(nums)):
            num = nums[i]

            # find the successor of current element
            if sorted_set and sorted_set.bisect_left(num) < len(sorted_set):
                if sorted_set[sorted_set.bisect_left(num)] <= num + t:
                    return True

            # find the predecessor of current element
            if sorted_set and sorted_set.bisect_left(num) != 0:
                if num <= sorted_set[sorted_set.bisect_left(num) - 1] + t:
                    return True

            sorted_set.add(num)
            if len(sorted_set) > k:
                sorted_set.remove(nums[i - k])

        return False


if __name__ == '__main__':
    s = Solution()
    # print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
