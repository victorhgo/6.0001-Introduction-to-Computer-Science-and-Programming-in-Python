# Lecture 3 - String Manipulation, Guess and Check, Approximations, Bisection

String manipulation, guess-and-check algorithms, approximate solution methods and bisection search.

- String manipulation

Strings are sequence of case sensitive characters, they can be compared with ==, >, <...

len() returns the length of the string

Example:

```py
string = "abc"
len(string) # will return 3
```

Square brackets for indexing strings: string[0] = a...

They can be sliced using [start:stop:step]
if give two numbers [start:stop], step=1 default

can also omit numbers and leave just colons

```py
string = "abcdefgh"
string[3:6] # > "def"
string[3:6:2] # > "df"
string[::] # > entire string, same as s[0:len(string):1]
string[::-1] # > 'hgfedcba', same as [-1:-(len(string)+1): -1] - Inverse of a string
string[4:1:-2] # 'ec', backwards
```

Keep in mind that strings are *immutable*, but we can *create* a new string and bound _string_ to the new one as:

```py
>>> string = "abcdefgh"
>>> string = 'y' + string[1:len(string)]
>>> string
'ybcdefgh'
>>>
```

- Strings and loops

```py
string = "abcdefgh"

for char in string:
    if char == 'i' or char == 'u':
        print("There is an i or u")
```

## Algorithms

We will be using the following algorithms, all in the context of solving an issue: finding the cube root for a number $n$. Remember that cube root is equal to:

$$\sqrt[3]{n}$$

> Guess and Check
For guess and check, also called _exhaustive enumeration_, we will follow the steps (recipe):

1. given a problem
2. able to guess a value for solution
3. check if the solution is correct
4. keep guessing until find solution *or* guessed all values

Example:

- Find the square root of number 8:

```py
cube = 8

for guess in range(cube + 1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)

# Cube not being a perfect cube, won't print anything
if guess ** 3 != abs(cube):
    print(cube, " is not a perfect cube")
```

Where a complete approach for this algorithm is:

```py
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
```

!!! S Note that _Exhaustive enumeration_ only works if the set of values being searched includes the value.

_abs() function returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude._

> Approximate Solutions
gives a good enough solution.

1. Starts with a guess and increment by some _small values_
2. keep guessing if |guess^3 - cube| >= epsilon for some small epsilon

Notes:

1. decreasing increment size >> slower program
2. increasing epsilon >> less accurate answer

Implementation of approximate solution for cube root:

```py
# Initializing variables
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

# Processing
while abs(guess**3 - cube) >= epsilon and guess <= cube :
    guess += increment
    num_guesses += 1

print('num_guesses = ', num_guesses)

if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess "is close to the cube root of", cube)
```

> Bisection Search
It searches half interval each iteration, and new guesses will be halfway in between.

- Game guessing a number

1. search space
    - first guess: $N/2$
    - second guess: $N/2$
    - k guess: $N/2^k$

2. guess converges on the order of $\log_2(N)$ steps

3. bisection search works when value of function varies monotonically with input (what does that mean?)

4. code as shown only works for positives cubes > 1 (why?)

5. modify to work with negative cubes (x < 1)

x < 1:
if x < 1, search space is 0 to x but cube root is greater than x and less than 1

> Exercise: Modify the code to work for finding an approximation to the cube root of both negative numbers and positive number.

_Answer_: By changing the _low_ statement from $0.0$ to _min(1.0, x)_ (The min() function returns the item with the lowest value, or the item with the lowest value in an iterable) we ensure that the answer will lies within the region being searched. In case of a negative number x, lower will receive _lower = -x_.


