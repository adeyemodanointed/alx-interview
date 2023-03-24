#!/usr/bin/python3
"""Function to generate pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle function"""
    our_list = []
    for i in range(n):
        mini_list = []
        for j in range(i + 1):
            mini_list.append(factorial(i)//(factorial(j)*factorial(i-j)))
        our_list.append(mini_list)
    return our_list


def factorial(n):
    """Function to calculate factorial"""
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
