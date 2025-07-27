"""
Exercise 2 - Write a function `fibonacci(n)` that returns the nth Fibonacci number using recursion.

Fibonacci is defined by: F(n) = F(n - 1) + F(n - 2)
"""

def Fibonacci(n):
    """
    Assumes x is an integer >= 0
    Returns Fibonacci of x
    """
    if n == 0 or n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    

print("Number of female rabbits after 12 months:", Fibonacci(12))

# Fibonacci with a dictionary: (Comparing using memoization)
# It will do a lookup first in case it already calculated the value and
# modify dictionary as progress through function calls:

print("Let's run the efficient one:")
def FibonacciEfficient(number, dictionary):
    if number in dictionary:
        return dictionary[number]
    else:
        answer = FibonacciEfficient(number - 1, dictionary) + FibonacciEfficient(number - 2, dictionary)
        dictionary = answer
        return answer

dictionary = {1:1, 2:2}

print("Efficient form of Fibonacci F(12):",FibonacciEfficient(12, dictionary))

