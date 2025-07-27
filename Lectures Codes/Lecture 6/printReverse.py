"""
Exercise 5 - Write a recursive function `print_reverse(n)` that prints numbers from `n` to `1`.
"""
def printReverse(n):
    """
    Assumes n is a positive integer >= 1
    Returns each number from n to 1
    """
    if n == 1: # Base case
        return n
    else:
        return printReverse(n - 1)

print(printReverse(3))