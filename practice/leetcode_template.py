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
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[first_zero_index] = nums[first_zero_index], nums[i]
                first_zero_index += 1




if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))
