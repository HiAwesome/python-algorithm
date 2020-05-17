"""
找零钱：动态规划
"""
import time


def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount

    return minCoins[change]


if __name__ == '__main__':
    start = time.time()
    print(dpMakeChange([1, 5, 10, 25], 63, [0] * 64))
    print(time.time() - start)

"""
6
0.00010204315185546875
"""
