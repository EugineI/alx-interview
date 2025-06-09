#!/usr/bin/python3
""" fewest number of coins"""


def makeChange(coins, total):
    """ reurn fewest no. of coins """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
