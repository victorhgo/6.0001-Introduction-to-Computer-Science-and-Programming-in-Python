# Lecture 6 - Recursion and Dictionaries

In today's class we will study Recursion (or divide/decrease and conquer) and dictionaries, which is another **mutable** object type

## Recursion

Recursion is the process of repeating items in a self-similar way. 

Algorithmically: a way to design solutions to problems by **divide and conquer** or **decrease and conquer**. In this method, we reduce a problem to simpler version of the same problem. 

Semantically: a programming technique where a **function calls itself** and the goal is to **NOT** have infinite recursion, otherwise the program will enter a infinite loop that can crash the entire system. 

It must have one or more *base cases* that are easy to solve, and then it must solve the same problem on **some other input** with the goal of simplifying the larger problem input.

So far we've been using iterative algorithms like looping constructs (_for_ and _while_) that can capture computation in a set of _state variables_ that update on each iteration through loop. One example is the **Multiplication** operation that iterative can be described as:

- _multiply x * y_ is equivalent to _add x to itself y times_, example:

$$4 * 5 = 4 + 4 + 4 + 4 + 4 = 20$$

It captures the state by an iteration number (i) starting at 5:
 i < i - 1 and stops when i = 0

and a current value of computation (the result):
result < result + x

We can write multiplication as an iterative solution in the way:

```py
def multiplicationIterative(x, y):
    """
    Input x and y as integers
    Returns the multiplication x * y
    """
    result = 0
    while y > 0:
        result += x
        b -= 1
    return result
```

But multiplication can be written as a recursive solution. First we think in the recursive step, how can we reduce this problem into a simpler/smaller version of the same problem?

If $x * y = x + x + x ... + x$ $(y)$ times, we can also describe $x * y = x + x + ... + x$ $(y - 1)$ times, in this way, we can think the multiplication in the recursive reduction:

$$x * y = x + x * (y - 1)$$

In the **base** case, we keep reducing the problem until we reach a simple case that can be solved directly. For instance, when $y = 1$, $x * y = x$. Then we can write the multiplication using the recursive solution as:

```py
def multiplication(x,y):
    """
    Receives x and y as integers
    Returns the multiplication x * y
    """
    if y == 1:
        return x
    else:
        return x + multiplication(x, y-1)
```

The **factorial** of a number is also a recursive operation.

Let $n$ be an integer such that:

$$n! = n * (n - 1) * (n - 2) * (n - 3) * ... * 1$$

Since we now that when $n - 1$ then $n! = 1$ (**base case**), we can reduce the problem as $n * (n - 1)!$. We can write a factorial function as:

```py
def factorial(x)
    """
    Receives an integer x
    Returns its factorial x!
    """
    if x == 1: # Base case
        return 1
    else:
        return x * factorial(x - 1)
```

Keep in mind that each recursive call to a function creates its own scope/environment, so bindings of variables in a scope are not changed by recursive call, and the flow of control passes back to previous scope once a function call returns a value.

Recursion may be simpler and more intuitive from the programmer perspective, more efficient too, but from the computer perspective, recursion may not be very efficient and if used wrongly, it can lead to infinite loops and unpredictable software behavior.

## Inductive Reasoning and Mathematical Induction

How do we know that our recursive code will work?

**Mathematical Induction**: To prove a statement of indexed on integers if true for all values of n:
- Prove it is true when n is the smallest value (example: $n = 0$ or $n = 1$)
- Then, prove that if it is true for any arbitrary value of $n$, it must be true for $n + 1$

Example:

We want to prove that $0 + 1 + 2 + 3 + ... + n = (n(n + 1))/2$, to do that:

If $n = 0$, then left hand side is $0$ and right hand side is $0 * 1/2$, so true:

$$0 = (0 + 1)/2$$

Assume it's true for some $k$, then we need to show that:

$$0 + 1 + 2 + ... + k + (k + 1) = ((k + 1)(k + 2))/2$$

So left hand side will be $k(k + 1)/2 + (k + 1)$ by assumption that property holds for problem of size $k$, so by algebra:

$$((k + 1)(k + 2))/2$$

When we think of recursion, the same logic used in induction applies to it. In the **base case** we show that the function must return a correct answer, so in the recursive call, we show it must also return a correct answer for problem of different size. Thus by induction, the program will return answer.

### Hanoi Tower

The problem:

- 3 tall spikes
- A stack of 64 different sized discs (starting on one spike)
- Need to move stack to second spike (at which point universe ends)
- But, can only move one disc at a time, and a larger disc can never cover up a small disc

> Exercise: After seeing a set of examples of different sized
stacks, how would you write a program to print out the
right set of moves? **Think recursively**: Solve a smaller problem, solve a basic problem, solve a smaller problem

```py
def printMove(from, to):
    print('move from',str(from),'to',str(to))

def Towers(n, from, to, spare):
    if n == 1:
        printMove(from, to)
    else:
        Towers(n - 1, from, spare, to)
        Towers(1, from, to, spare)
        Towers(n - 1, spare, to, from)     
```

### Fibonacci Numbers

Fibonacci modeled the following challenge:
Newborn pair of rabbits (one female, one male) are put in a pen, rabbits mate at age of one month, rabbits have a one month gestation period, assume rabbits never die and that female always produce one pair (one male, one female) every month from its second month on, how many female rabbits are there at the end of one year?

| Month | Amount of Females |
| --- | ---- |
|  0  |  1   |
|  1  |  1   |
|  2  |  2   |
|  3  |  3   |
|  4  |  5   |
|  5  |  8   |
|  6  |  13  |
|  7  |  21  |
|  8  |  34  |
|  9  |  55  | 
|  10 |  89  |
|  11 |  144 |
|  12 |  233 |

In general, females(n) = females (n - 1) + females(n - 2)
- Every female alive at mont $n - 2$ will produce one female in month $n$
- These can be added those alive in month $n - 1$ to get total alive in month $n$

### Recursion on non Numerics

How to check if a string of characters is a palindrome? "A palindrome is a word, phrase, name, or number that reads the same forward or backward".

First step to check if a string is a palindrome, we need to get rid of everything except characters (punctuation, spaces), convert everything to lower case then test it:

- If the string has length 0 or 1, it is a palindrome (**Base Case**)
- Recursive case: If first character matches last character, then is a palindrome if middle section is a palindrome

> Example: "Able was I, ere I saw Elba" removing every punctuation and spaces -> it becomes -> "ablewasiereisawelba"

```py
def isPalindrome(string):
    """
    Receives an string, converts everything to chars and lower case using
    toChars(string) function, which will return a list to isPal(string) that
    verifies if string is a palindrome.

    Return True if string is a palindrome, and False otherwise.
    """
    def toChars(string):
        string = string.lower()
        ans = ''
        for ch in string:
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + ch
        return ans
    
    def isPal(string):
        if len(string) <= 1:
            return True
        else:
            return string[0] == string[-1] and isPal(string[1:-1])
    
    return isPal(toChars(string))

# Output:
napoleon = "Able was I, ere I saw Elba"
print("Is,'", napoleon, "' a palindrome?", isPalindrome(napoleon))
```
Execution of the above code:

```sh
$ python3 palindrome.py
Is,' Able was I, ere I saw Elba ' a palindrome? True
```

## Dictionaries

A dictionary is good to index item of interest directly (not always an integer), and only requires one data structure. It stores pairs of data: a key and a value:

| Key  | Value |
| ---  | ---  |
| key1 | val1 |
| key2 | val2 |
| key3 | val3 |
| key4 | val4 |
| ...  | ...  |

To declare a dictionary:

```py
myDictionary = {} # Empty Dictionary
grades = {'Ana':'B', 'John':'A+', 'Victor':'A'}
```

It's similar to indexing into a list, but instead of a index integer, it will looks up the **key** and returns the value associated with it. If key is not found, get an error:

From the above example:

```py
grades['John'] # -> Returns 'A+'
grades['Julian'] # -> gives a Key Error
```

Since dictionaries are mutable, we can add entries by simply giving a key and associating a value to it:

```py
grades['Julian'] = 'B'

# It will now become:
grades = {'Ana':'B', 'John':'A+', 'Victor':'A', 'Julian':'B'}
```

We can also test if a key is in dictionary:

```py
'Victor' in grades # -> Returns True
'Danielle' in grades # -> Returns False
```

We can also remove an entry:

```py
del(grades['Ana'])
```

We can also get an iterable that acts like a tuple of all keys.

```py
grades = {'Ana':'B', 'John':'A+', 'Victor':'A', 'Julian':'B'}
grades.keys() # -> returns ['Ana', 'John', 'Victor', 'Julian']
```

Or we can get an iterable collection of all values:

```py
grades = {'Ana':'B', 'John':'A+', 'Victor':'A', 'Julian':'B'}
grades.values() # -> returns ['B', 'A+', 'A', 'B']
```

Note that the key must be **unique** and **immutable** for each dictionary.

| Some common operations on dictionaries includes: |
| --- |
| **len(dictionary)** returns the number of items in _dictionary_ |
| **dictionary.keys()** return the keys on _dictionary_ |
| **dictionary.values()** returns the values on _dictionary_ |
| **key in dictionary** returns **True** if the key _key_ is in _dictionary_ |
| **dictionary[key]** returns the item in _dictionary_ with key _key_ |
| **dictionary.get(k, v)** returns dictionary[k] if k is in _dictionary_, and _v_ otherwise |
| **dictionary[k] = v** associates a value _v_ to the key _k_. The value is replaced |
| **del dictionary[k]** removes the key _k_ from _dictionary_ |
| **for key in dictionary** iterates over the keys in _dictionary_ |


## Dictionary, Recursion and Memoization

Write more here


