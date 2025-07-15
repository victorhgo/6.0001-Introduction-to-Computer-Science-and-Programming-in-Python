# Lecture 4 - Decomposition, Abstraction and Functions

- [X] Reading of Chapters 4.1–4.2 and 4.4–4.6

How to structure our programs? We can use functions to organize the code better, hiding details and making it easier to debug, which will be a mechanism to achieve _decomposition_ and _abstraction_. To implement a basic function that checks if a number is even or not:

```py
def isEven(x):
    """
    Input: x, a positive integer
    Returns True if x is even, otherwise False
    """
    return x % 2 ==0
```

The function _isEven()_ accepts an integer x as _parameter_ (or _arguments_), the _docstring_ is a objective documentation (or specification) for the function in triple quotes, and the _body_ is what the function actually does. It is a best practice to use the keyword _return_ to return the expected function's result (True or False, for _isEven() function).

To call this function during execution, we can simply use its name and the values for parameters:

```py
isEven(5) # Returns False
isEven(4) # Returns True
```

- _Abstraction_ idea: You don't need to know how a tool works to use it, in case of programs, you don't need to know how a function works to use them.

- _Decomposition_ idea: You can use different devices working together to achieve an end goal, in case of programs, you can use a lot of functions working together to achieve a bigger goal.

#### Create Structure with Decomposition:
1. Divide Code into _modules_ where:
- they are *self contained*(mini programs where you feed an input, they do a small task and returns something)
- used to *break up* code
- intended to be *reusable*
- keep code *organized*
- keep code *coherent*

We can achieve decomposition with _functions_ (and later with _classes_ (Object Oriented Programming))

#### Suppress details with Abstraction:
2. A function is a *black box*:
- cannot see details
- do not need/want to see details
- hide tedious details

We can achieve Abstraction with _function specifications (docstring)_

### Scope of Variables

Scope means environment, so the scope of a function is a different environment than the main environment, so a formal parameter gets bound to the actual parameter of the function called. 

If you don't specify a return for the function, Python will returns _None_ as default
 
## Python Tutor

[Python Tutor](https://pythontutor.com/python-compiler.html#) - Good for debugging programs

> Fingertip exercise 1: Write a function isln that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and false otherwise. Uses built in str operation in
Done, check /Lectures Codes/Lecture 4/exercise1.py

### Modules

We can store parts of a program in different files for convenience and making it easy to organize and maintain. A *module* is a _.py_ file that contains Python definitions and statements, example is the _circle.py_:

```py
#circle.py

pi = 3.14159

def area(radius):
    return pi*(radius**2)

def circumference(radius):
    return 2*pi*radius

def sphereSurface(radius)
    return 4.0*area(radius)

def sphereVolume(radius)
    return (4.0/3.0)*pi*(radius**3)
```

We simply import the _circle.py_ whenever we want to access it's definitions and statements: 

```py
import circle
```

> Note: circle.py is only accessible this way if the program calling it is in the same directory, otherwise we need to specify the path to it

Modules usually are stored into individual files and each one has its own private symbol table

When we execute the statement _from MODULE import *_ we can omit the module name when accessing names defined inside the imported module.

A module can contain function definitions and also executable statements, usually to initialize the module.

### Files

Python has some built in facilities when dealing with files, they're called *file handle*. The following code is an example of opening a file named _log.txt_ in write mode, then you can enter a date and then closes the file:

```py
dateHandle = open('log.txt','w')
for i in range(2):
    date = input("Enter date: ")
    dateHandle.write(date + '\n')

dateHandle.close()
```

The _\n_ indicates a new line character (same way as in C language).

To read the data inside _log.txt_, we can use the function _open()_ in read mode. Note that Python treats a file as a sequence of lines:

```py
dateHandle = open('log.txt','r')

for line in dateHandle:
    print(line)

dateHandle.close()
```


