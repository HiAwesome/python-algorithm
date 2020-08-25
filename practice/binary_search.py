# https://leetcode-cn.com/problems/binary-search/
def binary_search(nums, target):
    if not nums:
        return -1

    if nums[0] > target or nums[-1] < target:
        return -1

    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1

    return -1

if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 5))
