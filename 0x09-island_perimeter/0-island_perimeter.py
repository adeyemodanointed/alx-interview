#!/usr/bin/python3
"""Island Perimiter Task"""


def island_perimeter(grid):
    """Island Perimeter function"""
    if (len(grid) == 0 or len(grid[0]) == 0):
        return 0

    result = 0
    connection = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 1):
                result += 4

                if (i > 0 and grid[i - 1][j] == 1):
                    result -= 2

                if (j > 0 and grid[i][j - 1] == 1):
                    result -= 2

    return result
