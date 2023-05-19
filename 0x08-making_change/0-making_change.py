#!/usr/bin/python3
"""Making a change interview question"""


def makeChange(coins, total):
    """Function that makes the change"""
    if total < 0:
        return 0

    dyn_arr = [float('inf')] * (total + 1)
    dyn_arr[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dyn_arr[i] = min(dyn_arr[i], dyn_arr[i - coin] + 1)

    if dyn_arr[total] == float('inf'):
        return -1

    return dyn_arr[total]
