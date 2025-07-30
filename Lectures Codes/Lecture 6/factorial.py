""" Exercise 1 - Write a function `factorial(n)` that returns the factorial of a number using recursion.
by Victor Correa
'"""
def Factorial(n):
    """
    Assumes n is an integer
    Returns the factorial of n in form of n!
    """
    try:
        if n == 0 or n == 1: # Base cases
            return 1
        else:
            return n * Factorial(n - 1)
    except:
        raise TypeError("Factorial got bad arg")
    
def testFactorial():
    """
    Let's get some arbitrary values for factorial including integers, floats and mixed types
    """
    # Integers greater than 1 and less than 10
    for n in range(1, 10):
        print(n, "! =", Factorial(n))
    
    # Some negative values:
    for n in [-2, -10, -6]:
        print(n, "! =", Factorial(n))

testFactorial()