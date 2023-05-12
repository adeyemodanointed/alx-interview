#!/usr/bin/python3
"""Rotate 2D-matrix algorithm"""


def rotate_2d_matrix(matrix):
    """Brute-Force method"""
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range (r - l):
            t, b = l, r
            t_l = matrix[t][l + i]
            matrix[t][l + i] = matrix[b - i][l]
            matrix[b - i][l] = matrix[b][r - i]
            matrix[b][r - i] = matrix[t + i][r]
            matrix[t + i][r] = t_l
        r -= 1
        l += 1
