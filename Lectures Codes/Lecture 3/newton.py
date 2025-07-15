# Newton-Raphson implementation

# 1. Inputs
epsilon = 0.01
x = 24.0
guess = x/2.0
iterations = 0

# 2. Processing
while abs(guess*guess - x) >= epsilon:
    guess = guess - (((guess**2) - x)/(2*guess))
    iterations += 1

# 3. Output
print("Square root of", x, "is about", guess)
print("Number of iterations", iterations)
