def isBigger(x, y):
    """
    Assumes x and y are ints
    Returns True if x is less than y and False otherwise
    """
    if x > y:
        return True
    else:
        return False
    
def test():
    """ 
    Let's choose some arbitrary values for x and y and test isBigger() function
    """
    for x in [-2, -1, 0, 1, 2]:
        for y in [-2, -1, 0, 1, 2]:
            print("Test for x = ", str(x), "and y = ", str(y))
            print("Is x bigger than y: ", isBigger(x, y))

test()