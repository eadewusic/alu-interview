#!/usr/bin/python3
"""
0-rain.py File
"""


def rain(walls):
    """
    Calculate how many square units of water will be 
    retained after it rains.

    Args:
        walls: A list of non-negative integers representing 
        the heights of walls.

    Returns:
        Integer indicating total amount of rainwater retained.
    """
    if not walls:
        return 0

    total_water = 0
    left_max = [0] * len(walls)
    right_max = [0] * len(walls)

    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[len(walls) - 1] = walls[len(walls) - 1]
    for i in range(len(walls) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    for i in range(len(walls)):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water


if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))  # Output: 6

    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))  # Output: 6
