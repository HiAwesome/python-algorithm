"""
找零钱：递归 + 记忆化
"""
import time


def recDc(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]

    for i in [c for c in coinValueList if c <= change]:
        numCoins = 1 + recDc(coinValueList, change - i, knownResults)

        if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins

    return minCoins


if __name__ == '__main__':
    start = time.time()
    # 这里因为需要求数字是 63 美分的最小零钱个数，因而初始化一个 64 位的 0 数组进行初始化，后面用于记忆对应位置的最小零钱个数
    print(recDc([1, 5, 10, 25], 63, [0] * 64))
    print(time.time() - start)

"""
6
0.00017309188842773438
"""
