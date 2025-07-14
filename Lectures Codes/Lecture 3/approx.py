cube = 10000
epsilon = 0.01

guess = 0.0
increment = 0.0001
numGuesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube :
    guess += increment
    numGuesses += 1

print('numGuesses = ', numGuesses)

if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)

else:
    print(guess, "is close to the cube root of", cube)