""" Exercise 1 - Write a function `factorial(n)` that returns the factorial of a number using recursion.
by Victor Correa
'"""
def Factorial(n):
    """
    Assumes n is an integer
    Returns the factorial of n in form of n!
    """
    if n == 0 or n == 1: # Base cases
        return 1
    else:
        return n * Factorial(n - 1)
    
print("5! = ", Factorial(5))
print("4! = ", Factorial(4))
print("3! = ", Factorial(3))
print("2! = ", Factorial(2))
print("1! = ", Factorial(1))
print("0! = ", Factorial(0))