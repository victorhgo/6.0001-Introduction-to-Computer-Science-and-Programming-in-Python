def findRoot(x, power, epsilon):
    """
    Assumes x and epsilon int or float, power an int,
        epsilon > 0 and power >= 1
    Returns float y such that y**power is within epsilon of x.
        If such a float does not exist, it returns None
    """

    # Because negative numbers has no even-powered roots
    if x < 0 and power % 2 == 0:
        return None
    
    low = min(-1.0, x)
    high = max(1.0, x)
    answer = (high + low) / 2.0
    while abs(answer**power - x) >= epsilon:
        if answer**power < x:
            low = answer
        else:
            high = answer
        
        answer = (high + low) / 2.0
    
    return answer

def testFindRoot():
    """
    This function tests if findRoot() works as intended by entering some
        arbitrary values for x and power
    """
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1, 4):
            
            print("Testing x =", str(x), "and power = ", power)
            result = findRoot(x, power, epsilon)

            if result == None:
                print(" No root for x = ", x, "and power = ", power)
            else:
                print("Result: ", result**power, "~=", x)

testFindRoot()

