"""
找零钱：使用递归方式解决
"""
import time


def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1

    for i in [c for c in coinValueList if c <= change]:
        numCoins = 1 + recMC(coinValueList, change - i)
        if numCoins < minCoins:
            minCoins = numCoins

    return minCoins


if __name__ == '__main__':
    start = time.time()
    print(recMC([1, 5, 10, 25], 63))
    print(time.time() - start)

"""
6
29.08635902404785
"""
