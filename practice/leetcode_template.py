from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        for index, value in enumerate(list1):
            dic[value] = index

        res = []

        min_sum = float('inf')

        for index, value in enumerate(list2):
            if index <= min_sum:
                if list2[index] in dic:
                    sum1 = index + dic[list2[index]]
                    if sum1 < min_sum:
                        res.clear()
                        res.append(list2[index])
                        min_sum = sum1
                    elif sum1 == min_sum:
                        res.append(list2[index])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findRestaurant(['tom', 'nancy'], ['jack', 'tom', 'nancy']))
