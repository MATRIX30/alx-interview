#!/usr/bin/python3
"""
make change money module
"""


def makeChange(coins: list, total: int) -> list:
    """
    returns the fewest number of coins  needed to
    meet a given amount total
    Args:
                coins(list): list(piles) of denominational coins
                total(int): total amount needed to make the change
        Returns:
                change(list): lfewest list of coins needed to change total
    """
    if total <= 0:
        return 0
    if type(coins) != list:
        raise TypeError("coins must be a list of coins")
    # sort the list of coins in decreasing order
    coins.sort(reverse=True)
    change = []
    i = 0
    while total > 0 and i < len(coins):
        if total - coins[i] >= 0:
            change.append(coins[i])
            total = total - coins[i]
        else:
            i += 1
    if total != 0:
        return -1
    else:
        return len(change)
