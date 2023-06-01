#!/usr/bin/python3
"""Prime Game Algorithm Module"""


def isWinner(x, nums):
    """Check who is the winner of the prime game"""
    ben = 0
    maria = 0

    # Based on pattern discovered, ben always wins at a step of 3
    # Then wins the next which is 4.
    # Then the pattern repeats itself.

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
