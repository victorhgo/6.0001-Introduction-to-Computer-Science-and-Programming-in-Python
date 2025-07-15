# Implementation: Finding the cube root of a number by bisection using a function

# 1. User inputs
x = int(input("Enter an integer x: "))

# Bisection function implementation
def cubeRoot(x):
    """
    Input: integer x
    Returns: Approximation of cubeRoot using bisection method
    """
    low = min(1.0, x)
    high = max(1.0, x)
    epsilon = 0.01
    answer = (high + low) / 2.0

    while abs(answer**3 - x) >= epsilon:

        if answer**3 < x:
            low = answer
        else:
            high = answer

        answer = (high + low) / 2.0 

    return answer

# 3. Return values

print(cubeRoot(x), "is close to the cube root of", x)

# What can be changed to allow me to work with both negative and positive number?
# By adding min(1.0, x) to the low variable we can work with a range < 1
