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
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left, right = max(nums), sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7,2,5,10,8], 2))
