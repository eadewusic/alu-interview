#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

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

    # Initialize variables to keep track of current number and operations
    current = 1  # Start with one 'H' in the file
    operations = 0

    while current < n:
        if n % current == 0:
            # If current is a divisor of n, perform a Copy All and Paste operation
            current *= 2
            operations += 2
        else:
            # If current is not a divisor, perform a Paste operation
            current += current
            operations += 1

    return operations

# Testing the function with the provided examples
if __name__ == "__main__":
    n1 = 4
    print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))

    n2 = 12
    print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))

