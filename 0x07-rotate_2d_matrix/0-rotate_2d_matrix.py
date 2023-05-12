#!/usr/bin/python3
"""Rotate 2D-matrix algorithm"""


def rotate_2d_matrix(matrix):
    """Brute-Force method"""
    left, r = 0, len(matrix) - 1

    while left < r:
        for i in range(r - left):
            t, b = left, r
            t_l = matrix[t][left + i]
            matrix[t][left + i] = matrix[b - i][left]
            matrix[b - i][left] = matrix[b][r - i]
            matrix[b][r - i] = matrix[t + i][r]
            matrix[t + i][r] = t_l
        r -= 1
        left += 1
