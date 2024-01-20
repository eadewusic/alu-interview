#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters in the file.

    Args:
    - n (int): The target number of 'H' characters.

    Returns:
    - int: The minimum number of operations needed.

    If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations for each position
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed to reach 1 'H'
    dp[1] = 0

    # Iterate through each position and update the minimum operations
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]

# Testing the function
if __name__ == "__main__":
    n1 = 4
    print("Min number of operations to reach {} characters: {}".format(n1, minOperations(n1)))

    n2 = 12
    print("Min number of operations to reach {} characters: {}".format(n2, minOperations(n2)))

