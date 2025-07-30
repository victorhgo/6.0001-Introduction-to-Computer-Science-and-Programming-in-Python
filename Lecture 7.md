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

1- Unit testing: validate each piece of program by testing each function separately.

```py
def isBigger(x, y):
    """
    Assumes x and y are ints
    Returns True if x is less than y and False otherwise
    """
```

1. Intuitive: about the boundaries of a program (numerical programs for instance):

We could run it on every pair of integers, but since integers are infinite, we can run it on pairs of integers that have a reasonable probability of error if there's a bug in the program. So we need to find a collection of inputs, called **test suite** that has a high change of revealing bugs. In _isBigger()_ example, the set of possible inputs is all pair combinations of integers, like:

- x positive, y positive
- x negative, y negative
- x positive, y negative
- x negative, y positive
- x = 0, y = 0
- x = 0, y $\neq$ 0
- x $\neq$ 0, y = 0

2. If we cannot find natural partitions, we can use **random testing**. And more tests, more likely the code is correct.

By testing the implementation of at least one value from each subset, there is a probability (not guaranteed) of exposing a bug (_if existent_)

For almost programs, it's not that easy to find a good subset of inputs to test.

Once we have it, we can start doing tests. 3 general classes of tests:

2- Regression testing: add tests for bugs as you find them, catch reintroduced errors that were previously fixed

3- Integration testing: does overall program work? It's recommended to not rush to do this


### Black-Box Testing

This kind of test is constructed without looking at the code to be tested, allowing testers and implementers to test different scenarios and exploring paths through specifications (Reading the function specifications (docstring), for instance)

Since the test data is generated without knowledge of implementation, the tests need not to be changed when the implementation is changed.

In the following example:

```py
def sqrt(x, epsilon):
    """
    Assumes x and epsilon are floats and
        x >= 0
        epsilon > 0
    Returns result such
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

In **Glass-Box** testing we use the code itself to figure it out the tests conditions and design them. Glass-Box test suites are easier to construct than black-box ones because we **use the code** directly to guide the design of test cases. It is called **path complete** if every potential path through the program is tested at least once.

The problem with this kind of test, is when we encounter loops for instance. The test could pass in the loop many times or not passing at all missing paths. So we have some guidelines to help design such cases:

1. In branches, we must exercise all parts of conditions.

2. For loops, we must exercise: loop not entered, body of loop executed exactly once or more than once.

3. While loops, same as for loops but test all cases which leads to the loop exit.

For the above example, we have a function that returns the absolute value of n:

```py
def abs(n):
    """
    Assumes n is an integer
    Returns the absolute value of n:
        n if n >= 0 or -n otherwise
    """
    if n < -1:
        return -n
    else:
        return n
```

A path complete test (2 and -2) set could miss a bug, but also *abs(-1)* would incorrectly return -1. And we should test boundary cases: (when n = -1 is a boundary case)

**Debugging process**

We encountered a bug, what about the debugging process? Python tutor can be a good debugging tool, print statements too. But how to use the print statements correctly?

Since they're good at showing us what's happening inside a program, a good place to put them are inside functions, loops (what are the loop parameters and values), what functions return what values and so go on. We can also use the **bisection method** as a debugging tool.

Good debugging steps are:

1. Study the program's code, don't ask what's wrong because it's a part of the test cases to figure out what's wrong, but ask how did we get an unexpected result.

2. Use the scientific method: study all the available data, form hypothesis and design experiments, pick simple inputs to test with.

When we are debugging we will come across error messages, like:

1. Trying to access beyond a limit of a list will give us *IndexError*
2. Trying to convert an inappropriate type will give us *TypeError*
3. Referencing  an inexistent variable will give us a *NameError*
4. Mixing data types without appropriate coercion will give us a *TypeError*
5. Forgetting to close parenthesis, quotations will give a *SyntaxError*

But **logical errors** are the hardest part to debug (always try to keep a good logical path to your code, explaining each step and validating it). To avoid logical errors and also make our life easier when developing a program:

Never write the entire program at once, or test it and debug it all at once. Instead:

Write a function, test the function and debug it. Then do it for another function and so on... And finally do the **integration test**

If changing a code, well document what's being change and save a backup!

## Exceptions and Assertions

### Exceptions

All the errors message above are example of exceptions:

- **SyntaxError** means that Python can't parse the program
- **NameError** local or global name not found
- **IOError** I/O system report malfunction (file not found, for instance)

We can have some exceptions handlers, for instance:

```py
try:
    a = int(input("Type a number"))
    b = int(input("Type another number"))
    print(a/b)
except:
    print("Bug in user input")
```

Any exception raised by any statement in body of _try_ will be handled by _except_ statement and execution will continue with the _except_ statement's body.

But we can be even more specific and catch specific errors, like:

```py
try:
    a = int(input("Type a number: "))
    b = int(input("Type another number: "))
    print("a / b =", a/b)
    print("a + b =", a + b)
except ValueError:
    print("Could not convert to an integer")
except ZeroDivisionError:
    print("Division by zero can't be handled")
except: # Any other possible error
    print("Error!") 
```

Some other rarely used exceptions are,

1. _else:_
- Will be executed when a _try_ block is completed **with no exception**

2. _finally:_
- Will be executed after _try, else, except_ clauses, even if they raised an error or executed a _break, continue, return_. They are ideally used for clean-up code that should be run no matter what else happened (e.g. closing a file)

**What to do when we encounter an error?**

- Fail silently (substituting the entered value for a correct one, for instance, or just continuing execution) is not a good idea because user gets no warning.

- Return an error value, but what value to return? As complicated programs might need to check for a special value.

- Stop execution, signal error condition: raise an exception
in Python: ```raise Exception("describe the error")```

```py
raise <ExceptionName> (<Arguments>)

# Where Exception name is the name we want for the error
# Arguments is the error description
```

Example raising an exception for a function:

```py
def getRatios(list1, list2):
    """
    Assumes list1 and list2 are lists of equal length of numbers
    Returns a list containing list1[i]/list2[i] 
    """
    ratios = []
    for index in range(len(list1)):
        try:
            rations.append(list1[index]/list2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan = not a number
        except:
            raise valueError("getRatios called with bad arg")
    return ratios
```

### Assertions

Part of defensive programming, assertive statements put at the beginning or end of a function. They're used to assure the assumptions on computations are exactly what the functions expects it to be. Example:

```py
def Average(grades):
    """
    Assumes that grades is a list of student's grade
    Returns the average of grades
    """
    assert len(grades) != 0, 'no grades data'
    return sum(grades)/len(grades)
```

Where to use asserts?

- Spot bugs as soon as they're introduced
- Use as a supplement for testing
- Raise exceptions if user supplies bad data input
- Use them to:
1. Check types of arguments and values
2. Check the invariants of a data structure are met
3. Check the constraints of return values
4. Check for violations of constraints on a procedure



