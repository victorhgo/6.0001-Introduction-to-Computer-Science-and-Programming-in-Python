# Implementation: Finding the cube root of a number by bisection
x = 25
epsilon = 0.01
numGuesses = 0.0
# Modify to min(1.0, x) to work with negative numbers
low = min(1.0, x)
high = max(1.0, x)
guess = (high + low) / 2.0

while abs(guess**3 - x) >= epsilon:
    print("Low =", low, "High =", high, "Answer =", guess)

    if guess**3 < x:
        low = guess
    else:
        high = guess

    guess = (high + low) / 2.0
    numGuesses += 1

print("num_guesses: ", numGuesses)
print(guess, "is close to the cube root of", x)

# What can be changed to allow me to work with both negative and positive number?

