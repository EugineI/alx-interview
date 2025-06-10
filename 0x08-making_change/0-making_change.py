#!/usr/bin/python3
""" fewest number of coins"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != total + 1 else -1
