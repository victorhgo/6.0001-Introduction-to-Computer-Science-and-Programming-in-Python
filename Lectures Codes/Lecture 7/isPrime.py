def isPrime(x):
    """
    Assumes x is a non-negative integer
    Returns True if x is prime, False otherwise
    """
    # if x <= 2:
    #     return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(isPrime(1093))

# This code is wrong