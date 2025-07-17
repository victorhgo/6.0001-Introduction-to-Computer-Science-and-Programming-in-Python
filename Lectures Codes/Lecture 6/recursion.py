def multiplication(x,y):
    """
    Receives x and y as integers
    Returns the multiplication x * y
    """
    if y == 1:      # Base case
        return x
    else:
        return x + multiplication(x, y-1)

def factorial(x):
    """
    Receives a positive integer x
    Returns its factorial x! (integer)
    """
    if x == 1 or x == 0: # Base case
        return 1
    else:
        return x * factorial(x - 1)
    
print("2 * 5:", multiplication(2,5))
print("15! =", factorial(15))
print("0! =", factorial(0))
