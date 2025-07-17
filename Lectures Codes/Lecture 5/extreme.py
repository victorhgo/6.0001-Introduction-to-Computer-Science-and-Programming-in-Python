def extremeDividers(n1, n2):
    """
    Assumes that n1 and n2 are positive integers.
    Returns a tuple containing the smallest common divisor > 1 and the largest common divisor of n1 and n2.
    If there is no common divisor, returns (None, None)
    """
    minValue, maxValue = None, None

    for i in range(2, min(n1,n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minValue == None:
                minValue = i
            maxValue = i
        
    return (minValue,maxValue)


minDivisor, maxDivisor = extremeDividers(188, 244)

print("Smallest common divisor:", minDivisor, "Largest common divisor:", maxDivisor)

print("IDs of maxDivisor:", id(maxDivisor), "minDivisor:", id(minDivisor), "extremeDividers:", id(extremeDividers))