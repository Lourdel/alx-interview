#!/usr/bin/python3
"""Making change"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount total.
    Args:
    coins: A list of the values of the coins in your possession.
    total: The amount of change you need to make.

    Returns:
    The fewest number of coins needed to meet total.
    If total is 0 or less, returns 0.
    If total cannot be met by any number of coins you have, returns -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        coin_count += int(total // coin)
        total %= coin

    if total != 0:
        return -1
    else:
        return coin_count
