from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess) -> bool:
            count, left = 0, 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]

        while lo < hi:
            mi = lo + (hi - lo) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo


if __name__ == '__main__':
    s = Solution()
    print(s.smallestDistancePair([4, 5, 6, 7, 0, 1, 2], 0))
