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
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:

        # 核心思想--枚举前缀和后缀
        # 如果两个字符串k1，k2组成一个回文字符串会出现三种情况
        # len(k1) == len(k2),则需要比较k1 == k2[::-1]
        # len(k1) < len(k2),例如，k1=a, k2=abb,可组成abba
        #   因为k2后缀bb已经是回文字符串了，则需要找k1与k2剩下相等的部分
        # len(k1) > len(k2),例如，k1=bba, k2=a,组成abba
        #   因为k1前缀bb已经是回文字符串了，则需要找k1剩下与k2相等的部分

        res = []
        dic = {word: i for i, word in enumerate(words)}  # 构建一个字典，key为word，value为索引
        for i, word in enumerate(words):
            # i为word索引，word为字符串
            for j in range(len(word) + 1):
                # 这里+1是因为，列表切片是前闭后开区间
                prefix = word[:j]  # 字符串的前缀
                suffix = word[j:]  # 字符串的后缀
                if prefix[::-1] in dic and dic[prefix[::-1]] != i and suffix == suffix[::-1]:
                    # 当word的前缀在字典中，且不是word自身，且word剩下部分是回文(空也是回文)
                    # 则说明存在能与word组成回文的字符串
                    res.append([i, dic[prefix[::-1]]])  # 返回此时的word下标和找到的字符串下标

                if j > 0 and suffix[::-1] in dic and dic[suffix[::-1]] != i and prefix == prefix[::-1]:
                    # 当word的后缀在字典中，且不是word自身，且word剩下部分是回文(空也是回文)
                    # 则说明存在能与word组成回文的字符串
                    # 注意：因为是后缀，所以至少要从word的第二位算起，所以j>0
                    res.append([dic[suffix[::-1]], i])  # 返回此时的word下标和找到的字符串下标
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    # print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
    a = {(1, 2)}
    b = a | {(2, 3)}
    print(b)
    print(type(a))
