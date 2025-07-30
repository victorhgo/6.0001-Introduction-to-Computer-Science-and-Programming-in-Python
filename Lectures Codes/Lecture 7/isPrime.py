def isPrime(x):
    """
    Assumes x is a natural number > 1
    Returns True if x is prime, False otherwise
    """
    try:
        if x > 1:
            for i in range(2, x):
                if x % i == 0:
                    return False
                
            return True
        else:
            return False
    # If x is anything but an integer
    except:
        return None

def test():
    """
    Let's choose some arbitrary values for x and test whether they're prime or not, or if we find an issue with our program
    """
    # test for the first 100 integers:
    for x in range(1, 10):
        print("Is", x, "prime?", isPrime(x))
    # Negative, floats and characters
    for x in [6.7 , -83, 'a', None, 0]:
        print("Is", x, "prime?", isPrime(x))

test()

# Let's save a list of the first primes (from 0 to 100):
