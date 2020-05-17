"""
找零钱：动态规划 + 优化
"""
import time


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin

    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


if __name__ == '__main__':
    start = time.time()

    amnt = 63
    clist = [1, 5, 10, 25]
    coinsUsed = [0] * 64
    coinCount = [0] * 64

    print('Making change for %s requires.' % amnt)
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), 'coins')
    print('They are:')
    printCoins(coinsUsed, amnt)
    print('The used list is as follows:')
    print(coinsUsed)

    print(time.time() - start)

"""
Making change for 63 requires.
6 coins
They are:
1
1
1
10
25
25
The used list is as follows:

[1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 25, 
 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1, 1, 25, 
 1, 1, 1, 1, 5, 1, 1, 1, 1, 10, 1, 1, 1]

0.0001499652862548828
"""
