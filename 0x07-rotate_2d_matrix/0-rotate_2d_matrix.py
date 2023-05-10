#!/usr/bin/python3
"""Rotate 2D-matrix algorithm"""
import copy


def rotate_2d_matrix(matrix):
    """Brute-Force method"""
    rotated_matrix = copy.deepcopy(matrix)
    mat_len = len(matrix)
    for i in range(mat_len):
        for j in range(mat_len):
            matrix[i][j] = rotated_matrix[mat_len - 1 - j][i]
