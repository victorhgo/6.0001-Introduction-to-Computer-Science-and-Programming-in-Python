# Newton-Raphson implementation

# 1. Inputs
epsilon = 0.01
x = 728.0
guess = x/2.0
iterations = 0

# 2. Processing
while abs(guess*guess - x) >= epsilon:
    guess = guess - (((guess**2) - x)/(2*guess))
    iterations += 1

# 3. Output
print("Using Newton, square root of", x, "is about", guess)

# Implementation: Finding the cube root of a number by bisection
# 1. Inputs
numGuesses = 0.0
low = min(1.0, x)
high = max(1.0, x)
guess = (high + low) / 2.0

while abs(guess**3 - x) >= epsilon:

    if guess**3 < x:
        low = guess
    else:
        high = guess

    guess = (high + low) / 2.0
    numGuesses += 1

print("Using bisection,", guess, "is close to the cube root of", x)

# Comparison
efficiency = abs(numGuesses/iterations)

print("While Newton uses", iterations, "iterations to find the root, Bisection uses",numGuesses)
print("Which makes Newton method", efficiency, "times more efficient than bisection" )