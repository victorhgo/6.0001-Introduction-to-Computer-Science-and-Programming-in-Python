# Lecture 7 - Testing, Debugging, Exceptions and Assertions

In this lecture, we will learn about debugging, testing and exceptions/assertion statements in Python. 

## Testing, Defensive Programming and Eliminating source of the bugs

In the making soup analogy, check the soup for bugs is the **testing** part, where keep the lid closed is the action of **defensive programming** and cleaning the kitchen is **eliminating the source of bugs**.

In programming each of these actions to ensure high quality on the software can be done by following some good practices:

## Defensive Programming

We can achieve **defensive programming** attitude by writing specification for functions, making sure our program is well documented and avoiding unwanted behavior. By modularizing the code, writing it on different blocks and documenting everything that's happening on each block, we will have a better understanding on what's happening on the code and testing/debugging will be easier to perform.

Once we have a program that's modular and well documented, we still have to test it, and we can do it by checking all the conditions on the inputs and outputs. Given an input, if the output is what we expected then we are done with it. If not, then we can proceed to the debugging phase.

## Debugging and Testing

To **debug** a program we need to **study the events** that lead up to an error and check why is it not working and how to fix it. This part is not as easier, and the purpose of testing a program is not to show that a program is bug-free, but to shot that bugs exists. This happens because even the smallest program possible has billions of possible inputs. Using the program bellow as example:

1- Unit testing: validate each piece of program by testing each function separately

```py
def isBigger(x, y):
    """
    Assumes x and y are ints
    Returns True if x is less than y and False otherwise
    """
```

We could run it on every pair of integers, but since integers are infinite, we can run it on pairs of integers that have a reasonable probability of error if there's a bug in the program. So we need to find a collection of inputs, called **test suite** that has a high change of revealing bugs. In _isBigger()_ example, the set of possible inputs is all pair combinations of integers, like:

- x positive, y positive
- x negative, y negative
- x positive, y negative
- x negative, y positive
- x = 0, y = 0
- x = 0, y $\neq$ 0
- x $\neq$ 0, y = 0

By testing the implementation of at least one value from each subset, there is a probability (not guaranteed) of exposing a bug (_if existent_)

For almost programs, it's not that easy to find a good subset of inputs to test.

Once we have it, we can start doing tests. 3 general classes of tests:

1- Unit testing: validate each piece of program by testing each function separately

2- Regression testing: add tests for bugs as you find them, catch reintroduced errors that were previously fixed

3- Integration testing: does overall program work? Do not rush to do this

### Black-Box Testing

This kind of test is constructed without looking at the code to be tested, allowing testers and implementers to test different scenarios and exploring paths through specifications (Reading the function specifications, for instance)

Since the test data is generated without knowledge of implementation, the tests need not to be changed when the implementation is changed.

In the following example:

```py
def sqrt(x, epsilon):
    """
    Assumes x and epsilon are floats and
        x >= 0
        epsilon > 0
    Returns result such that
        x - epsilon <= result * result <= x+ epsilon
    """
```

In the specification above, there are only two distinctive paths: either x = 0 or x > 0. But it's not sufficient to test only both cases.

_Boundary conditions_ should also be tested in a black-box testing. If a list is the subject of test, we should look the empty list, a list with one element and a list with lists. When dealing with numbers, it means looking at very small and very large values and typical values. For _sqrt()_ above, we could look to values of x and epsilon similar to:

| Case | X | Epsilon |
| --- | --- | --- |
| boundary | 0 | 0.0001 |
| perfect square | 25 | 0.0001 |
| less than 1 | 0.05 | 0.0001 | 
| irrational square root | 2 | 0.0001 |
| extremes | 2 | 1.0 / 2.0**64.00 |
| extremes | 1.0 / 2.0**64.0 | 1.0 / 2.0**64.0 |
| extremes | 2.0**64.0 | 1.0/2.0**64.0 |
| extremes | 1.0 / 2.0**64.0 | 2.0**64.0 |
| extremes | 2.0**64.0 | 2.0**64.0 |

If any of these tests fail, something needs to be fixed in the code. It might be a bug or the specification that needs to be changed, or it might be not possible to find an approximation of a square root when epsilon is too small.

It's also important to think about aliasing as a boundary condition. For instance:

```py
def copy(list1, list2):
    """
    Assumes that list1 and list2 are lists;
    Mutates list2 to be a copy of list1
    """
    while len(list2) > 0:
        list2.pop()
    for element in list1:
        list2.append(element)
```

This program will work most of the time, but not when _list1_ and _list2_ refer to the same list, any test suit that did not include a call of the form _copy(list, list)_ would not reveal the bug.

### Glass-Box testing

Without looking the internal code structure, it's impossible to know which test cases are likely to provide new information. For instance:

```py
def isPrime(x):
    """
    Assumes x is a non-negative integer
    Returns True if x is prime, False otherwise
    """
    if x <= 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
```

This function is wrong because of the test _if x <= 2: return False_, which if called _isPrime(2)_ returns _False_, wrongly indicating that 2 is not prime.

Glass-Box test suites are easier to construct than black-box ones, we will **use code** directly to guide the design of test cases. It is called **path complete** if every potential path through code is tested at least once.

But this type of test can go through loops arbitrarily many times, missing paths. Consider the following case:

```py
def abs(x):
    """
    Assumes x is an int
    Return x if x >= 0 and -x otherwise
    """
    if x < -1:
        return -x
    else:
        return x
```

