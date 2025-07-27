"""
Exercise 4 - Write a recursive function `power(base, exponent)` to compute `base^exponent`
by Victor Correa
"""

def power(base, exponent):
    """
    Assumes both base and exponent are integers and exponent is positive
    Returns power in the form of base^exponent
        Note: it calculates a power in form of (base)^exponent, so for negative numbers expects (-base)^exponent
    """
    if exponent == 0:            # Base case 1: for all number n^0 = 1
        return 1
    
    elif exponent == 1:          # Base case 2: for all number n^1 = n
        return base
    
    elif base == 0 or base == 1: # Base case 3: 0^n = 0 and 1^n = 1
        return base
    else:                        # General case: 
        return base * power(base, exponent - 1)

# Tests with base 2
print("Test1: -2^3:", power(-2,3))
print("Test2: 2^6:", power(2,6))
print("Test2: -2^7:", power(-2,7))
print("Test3: 2^8:", power(2,8))
# Test with base 3
print("Test4: 3^2:", power(3,2))
print("Test5: 3^3:", power(3,3))
print("Test6: 3^8:", power(3,8))
# Test with base 16 (HEX)
print("Test7: 16^2:", power(16,2))
print("Test8: 16^3:", power(16,3))
print("Test9: 16^4:", power(16,4))