# Lecture 5 - Tuples, Lists, Aliasing, Mutability, and Cloning

In this lecture we are going to work with compound data types (tuples and lists), the concept of aliasing, mutability and cloning.

### Tuples

Tuples are an ordered sequence of elements (they can be different types), but tuples are *immutable* (strings for instance, are tuples), they're represented by parenthesis:

```py
tuple1 = () # Empty tuple
tuple2 = (1, "hello", 5) # Tuple with three elements

# Examples
tuple2[0]   # Evaluates to 1
tuple2[1:2] # Slice tuple, evaluates to ("hello",) <- extra comma means a tuple with one element

tuple2[1:3] # Slice tuple, evaluates to ("hello", 5)

len(tuple2) # Evaluates to 3 (size of tuple)

t[1] =  "bye" # Returns an error, you can't modify a tuple
```

_Important:_ - If a tuple with one element does not evaluate to (element, ), it means it's not a tuple, but a string instead.

They are used to *swap* variable values and when returning *more than one value* from a function, for instance:

```py
def quotientRemainder(x, y):
    quotient = x // y # Integer division
    remainder = x % y
    return (quotient, remainder)

(quot, rem) = quotientRemainder(7, 9) # Receive the values in a tuple
```

We can use tuples to easily *swap* variable values, like the following example

```py
temp = x
x = y
y = temp

# Is the same as 
(x, y) = (y, x)
```

#### Manipulating tuples

Tuples are really useful because they hold collection of data, they can also be iterated over. In the following function that can be applied to any set of data, you can extract some basic information from the data set.

aTuple should look similar to the structure _aTuple:((), (), ())_ and its elements are also tuples, where each tuple object are going to contain 2 elements, the first being an integer and the second a string, in the way: _aTuple:((int string), (int string), (int string))_ 

```py
def getData(aTuple):
    nums = ()       # <- It will create two empty tuples, nums and words
    words = ()      # <- second empty tuple words

    # Iterating over tuple objects
    for t in aTuple:
        nums = nums + (t[0],) # <- Singleton tuple (tuple of one element)
        if t[1] not in words:
            words = words + (t[1],)
    minN = min(nums)
    maxN = max(nums)
    uniqueWords = len(words)
    return (minN, maxN, uniqueWords)
```

#### Advantages of Tuples

Since tuples are immutables, they are very useful when it comes to aliasing, they will be really handy when it comes to *dictionaries*, because we can use tuples as keys in dictionaries.

### Lists

Are ordered sequence of information accessible by an *index*, they are denoted by square brackets *[]* and usually the elements of a list are homogenous (same type), it's not very common to contain mixed types. But different from tuples, lists can be changed (they're *mutable*). An example of a list:

```py
integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list = [] # <- Empty list

print("len(integers):", len(integers)) # <- Evaluates to 10
print("Integers[0]:", integers[0]) # <- Evaluates to 0
print("Integers[1] + 2:", integers[1] + 2) # <- Evaluates to 3

# Lists can contain other lists:

realNumber = [integers, 3.1415, [-2, -1, 0]]
print("realNumber[0]:", realNumber[0]) # <- Evaluates to [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], another list
print("len(realNumber):", len(realNumber)) # <- Evaluates to 3

print("realNumber[3]:", realNumber[2]) # <- Evaluates to [-2, -1, 0]
```

#### Changing elements of a list

Since lists are mutable, we can change the values by assigning to an element at an index to changes the value:

```py
list1 = [1, 2, 3]
list1[1] = 9

# Now list1 is:
[1, 9, 3]
```

It's important to note that: List elements are indexed from _0_ to _len(list) - 1_ and _range(n)_ goes from _0_ to _n - 1_

#### Operations on lists - ADD

We can *append* elements to end of list with _list.append(element)_, it mutates the list and add to the end:

```py
even = [2, 4, 6]
even.append(8)

# Even now will be:
[2, 4, 6, 8]
```

- Note: Everything in Python is an object! Objects have data, methods and functions, since lists are objects we can access this information by _objectName.doSomethin()_ in Python.

We can also combine lists together using *concatenation* + operator to give us a new list. To *mutate* a list with list.extend(anotherList):

```py
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 # list3 = [1, 2, 3, 4, 5, 6]

list1.extend([7, 8]) # > Mutate list1 to [1, 2, 3, 7, 8]
```

#### Removing elements from a list

We can delete an element at a *specific index* with _del(list[index])_, we can also remove the element at the *end of the list* with the _list.pop()_, this function returns the removed element.

We can also remove an specific element with _list.remove(element)_, what _remove()_ does:

- looks for the element and removes it
- if the element occurs multiple times, it will only remove the *first occurrence*
- if the element is not on the list, returns an error

!!! N Note that each of these operations mutate the list permanently!

```py
list4 = [1, 2, 3, 4, 5, 6, 7, 8]
list4.remove(1) # > Removes 1 from list
list4.remove(2) # > Removes 2 from list
del(list4[3])   # > Removes 5 from list
list4.pop()     # > Removes 8 from list
```

#### Convert lists to strings and back

We can also convert a *string* to a *list* by using _list(string)_, which will return a list with every character from string an element in list. This is really useful when dealing with data.

We can use the _string.split()_ to split a string on a character parameter, it will splits on spaces if called without a parameter.

We can use _''.join(list)_ to turn a *list of characters into a string*, it can be given a character in quotes to add char between every element.

```py
string = "My name is Victor"
list(string)

string.split('s')

list5 = ['a', 'e', 'i', 'o']
''.join(list5)
'_'.join(list5)
```

Other list operations includes _sort()_, _sorted()_, _reverse()_. Here's a guide to lists

[Data Structures in Python](https://docs.python.org/3/tutorial/datastructures.html)

### Mutation, Aliasing and Cloning

Important concepts, study more from the book too!!! Use Python tutor to help.

#### Mutation 

#### Aliasing

#### Cloning

It's a good idea to avoid mutating a list over which one is iterating. So we can clone a list using slicing (make a copy of a list). In the below function it will modify the value of list1:

```py
def removeDups(list1,list2):
    """
    Assumes that list1 and l2 are lists.
    Removes any element from List1 that also occurs in list2
    """
    for element in list1:
        if element in list2:
            list1.remove(element)
```

But we can avoid this by using slice to clone it:

```py
def removeDups(list1,list2):
    """
    Assumes that list1 and l2 are lists.
    Removes any element from List1 that also occurs in list2
    """
    for element in list1[:]:
        if element in list2:
            list1.remove(element)
```

Do some tests too.

!!! N Note finished yet!

### Object ID in Python

All objects in Python has a unique ID that can be verified by the built-in function _id_, and it returns a unique integer identifier for an object. It's syntax:

```py
id(objectName)

# Returns an integer value
print("ID objectName:" id(objectName))

# ID objectName: 4393380376
```

### List comprehension

It provides a concise way to apply an operation to the values in a sequence, it will create a new list in which each element is the result of applying a giving operation. For instance, we want to create the first 8 Base 2 numbers such that: In binary, each position represents a power of 2 ($2^0$, $2^1$, $2^2$, etc.).

```py
binary = [2**x for x in range(0,8)]
print(binary)

# will print [1, 2, 4, 8, 16, 32, 64, 128]
```

The for clause can be followed by one or more if and for statements that are applied to the values produced by the for clause. For example, the code:

```py
mixed = [1, 2, 'a', 3, 4.0]
print([x**2 for x in mixed if type(x) == int])

# Will print: [1, 4, 9] (only ints will be squared)
```

### Higher-Order Programming (Functions as Arguments)

Since functions are objects in Python, they are called *first-class objects*, that means they can be treated like objects of any other type. They also have types and they can appear in expressions like: as the right-hand side of an assignment statement, elements of lists, argument to another function...

Using functions as arguments will allow a style of coding called *higher-order programming*. When combining with lists, it can be really convenient. Example:

```py
def applyToEach(list, function):
    """
    Assumes list is a list, function is a function
    It mutates list by replacing each element e of list by function(e)
    """
    for i in range(len(list)):
        list[i] = function(list[i])
```

This function _applyToEach()_ is called higher-order because it has an argument that is itself a function. So the first time it's called, it mutates the list by applying the function passed as an argument to it.

A build-in higher-order function in Python is _map()_: [Python Docs](https://docs.python.org/3/library/functions.html#map)

```
map(function, iterable, *iterables)

Return an iterator that applies function to every item of iterable, yielding
the results. If additional iterables arguments are passed, function must take
that many arguments and is applied to the items from all iterables in
parallel. With multiple iterables, the iterator stops when the shortest
iterable is exhausted. For cases where the function inputs are already
arranged into argument tuples, see itertools.starmap().
```

#### Lambda Expression

Python allows the creation of an anonymous function (a function that is not bound by a name) using the reserved word *lambda*. The general form of a *lambda expression* is:

```py
lambda <sequence of variable names>:<expression>
```

For instance, if we use the lambda expression:

```py
lambda x, y : x * y
```

It will return a function that returns the product of its two arguments. Lambda expressions are frequently used as argument to higher order functions. Example at _/Lecture Codes/Lecture 5/lambda.py_.

### Summary of sequence types and their operations

Some common operations on sequences are:

- _seq[i]_ returns the _i_ element in the sequence
- _len(seq)_ returns the size (length) of the sequence
- _seq1 + seq2_ concatenates two sequences (not available for ranges)
- _n * seq_ returns a sequence that repeats seq n times (also not available for ranges)
- _seq[start:end]_ returns a slice of the sequence
- _e in seq_ is *True* if e is contained in the sequence, otherwise *False*
- _e not in seq_ is *True* if e is *not contained* in the sequence, otherwise *False*
- _for e in seq_ iterates of each element of the sequence

Comparison of sequence types:

| Type | Type of Elements | Example of literals | Mutable |
| --- | --- | --- | --- |
| str | characters | '', 'h', 'abc' | No |
| tuple | any type | (), (3,), ('hello', 5) | No |
| range | integers | range(10), range (1, 10, 2) | No |
| list | any type | [], [1, 2, 3], ['hello', [1, 2]] | Yes |