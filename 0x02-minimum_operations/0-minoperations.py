#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Given a number n, write a method that calculate
    the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    factors = []

    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                n = int(n / i)
                factors.append(i)
                break
    return sum(factors)
