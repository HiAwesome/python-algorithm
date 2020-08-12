from typing import List
import math

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
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum1 = sum(nums)
        all_sum = sum1 + S

        if sum1 < S or all_sum % 2 == 1:
            return 0

        p = all_sum // 2

        dp = [1] + [0 for _ in range(p)]

        for num in nums:
            for j in range(p, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[p]


if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
