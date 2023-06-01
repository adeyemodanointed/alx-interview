#!/usr/bin/python3
"""Prime Game Algorithm Module"""


def isWinner(x, nums):
    """Check who is the winner of the prime game"""
    if x == 0 or len(nums) == 0 or x is None or nums is None:
        return None
    ben = 0
    maria = 0
    for i in range(x):
        if nums[i] == 1:
            ben += 1
        elif nums[i] % 4 == 0 or nums[i] % 4 == 3:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    else:
        return None
