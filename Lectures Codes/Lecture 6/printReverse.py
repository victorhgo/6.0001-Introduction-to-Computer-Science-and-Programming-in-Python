"""
Exercise 5 - Write a recursive function `print_reverse(n)` that prints numbers from `n` to `1`.
"""
def printReverse(n):
    """
    Assumes n is a positive integer >= 1
    Returns each number from n to 1
    """
    if n <= 0: # Base case, when n <= 0 stops recursion
        return
    
    print(n) # Prints current value of n
    printReverse(n - 1) # Calls it recursively for n - 1 until n <= 0

# Non recursive solution:
def printRev(n):
    """
    Assumes n is a positive integer >= 1
    Returns each number from n to 1
    """
    if n == 1:
        print(n)

    while(n >= 1):
        print(n)
        n -= 1

printReverse(10)

#printRev(1)
#printRev(3)
printRev(10)
#printRev(20)