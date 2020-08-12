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
    def numSquares(self, n: int) -> int:
        square_nums = [i * i for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                else:
                    dp[i] = min(dp[i], dp[i - square] + 1)

        return int(dp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(12))
