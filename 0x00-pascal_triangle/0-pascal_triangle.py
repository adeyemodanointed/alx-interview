#!/usr/bin/python3
from math import factorial
"""Function to generate pascal triangle"""


def pascal_triangle(n):
    our_list = []
    for i in range(n):
        mini_list = []
        for j in range(i + 1):
            mini_list.append(factorial(i)//(factorial(j)*factorial(i-j)))
        our_list.append(mini_list)
    return our_list
