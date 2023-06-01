#!/usr/bin/python3
"""Prime Game Algorithm Module"""


def isWinner(x, nums):
    """Check who is the winner of the prime game"""
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
    else:
        return 'Maria'
