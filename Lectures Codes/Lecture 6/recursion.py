def multiplication(x,y):
    """
    Receives x and y as integers
    Returns the multiplication x * y
    """
    if y == 1:      # Base case
        return x
    else:
        return x + multiplication(x, y-1)
    
def test():
    """
    Select some arbitrary values for x and y to test multiplication
    """
    for x in range(1, 100):
        for y in range(1, 100):
            if multiplication(x,y):
                print("Pass")
            else:
                print("Error")

test()