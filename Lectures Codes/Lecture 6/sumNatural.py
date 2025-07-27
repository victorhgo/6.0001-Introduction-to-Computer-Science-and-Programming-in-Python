"""
Exercise 3 - Write a function `sum_natural(n)` that returns the sum of the first `n` natural numbers recursively.
"""

def sumNatural(n):
    """
    Assumes n is an positive integer
    Return the sum of each nth natural numbers
    """
    if n == 1:
        return 1
    else:
        return n + sumNatural(n - 1)
    
print("Test: sum(4)", sumNatural(4))
print("Test: sum(6)", sumNatural(6))