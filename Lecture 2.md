# Lecture 2: Branching and Iteration

String object type, branching and conditional, indentation and iteration and loops

Strings are enclose in quotation marks or single quotes and can contain characters, spaces, digits.

hi = "Hello there" 

We can _concatenate_ strings in Python:

```py
name = "Victor"

greet = hi + name

greeting = hi + " " + name
```

We can perform some operations on a string.

- OUTPUT : print
Output data on console

```py
x = 1
print(x)

x_string = str(x)

# Two ways of printing data in Python
print("A number", 1 , ".", "x =", x)
print("A number " + x_string + ". "+ "x = " + x_string)
```

- Input: input("")
Print what is on quotes, user can type in and binds that value to a variable:

```py
text = input("Type a text >>> ")

# Prints the string x times
print(5 * text)
```

- Comparison Operators on _int_, _float_, _string_

Where _i_ and _j_ are variable names, comparisons evaluates toa Boolean:

```py
i > j
i >= j
i < j
i <= j
i == j # Equality test
i != j # Inequality test
```

- Logical Operators on Booleans
Where _a_ and _b_ are variable names with Boolean values:

```py
not a # True if a is False, False if a is True

a and b # True if both are true

a or b # True if either or both are true
```

- Control flow, branching (if conditions)
Conditions has a value _True_ or _False_

```py
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))

if x == y:
    print("x and y are equal")
    if y != 0:
        print("Therefore, x / y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("Goodbye :)")
```

- Control flow: _while_ loops

```sh
while <condition>:
    <expression>
    <expression>
```

Where condition evaluates to a Boolean and if true, do all steps inside the while code block until condition is False.

- Control Flow: _for_ loops

```py
for <variable> in range (<number>):
    <expression>
    <expression>
```

In the form of:

```py
for n in range(5):
    print(n)
```

It will print n 5 times in the screen

- range(start, stop, step)
Range can be customized, where default values are _start = 0_ and _step = 1_ and optional loop until value is _stop - 1_.

Example:

```py
mysum = 0
for i in range(7, 10): # 7, 8, 9 (ends on n - 1)
    mysum += i
print(mysum)

# 0 + 7, 7 + 8, 15 + 9
# = 27
```

- _break_ statement
To immediately stops the execution of the loop, does not matter where it is in skipping remaining expressions in the code block, but only exits the innermost loop.

```py
while <condition_1>
    while<condition_2>
        <expression1>
        break
        <expression2>
    <expression3>
```

When to use _for_ loops or _while_ loops?

_for_ loops are used when you know the number of iterations, can end early via break, use a counter and can rewrite a _for_ loop using a _while_ loop.

_while_ loops have _unbounded_ number of iterations, can also end early via break, can use a counter but *must initialize* before loop and increment inside the loop to prevent infinite loop and may not be able to rewrite a _while_ loop using a _for_ loop.

