# Implementation: Finding the cube root of a number by Guess and Check
cube = 9
guess = int(input("Enter a guess: "))

for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break

# Cube not being a perfect cube, won't print anything
if guess ** 3 != abs(cube):
    print(cube, "is not a perfect cube")

else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + " is " + str(guess))