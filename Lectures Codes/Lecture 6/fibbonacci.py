def fib(x):
    """
    Assumes x an integer >= 0
    Returns Fibonacci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib (x - 2)
    

print("Number of female rabbits after 12 months:", fib(12))