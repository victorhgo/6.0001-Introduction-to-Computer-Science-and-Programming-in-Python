# Lecture 5 - Tuples, Lists, Aliasing, Mutability, and Cloning

In this lecture we are going to work with compound data types (tuples and lists), the concept of aliasing, mutability and cloning.

### Tuples

Tuples are an ordered sequence of elements (they can be different types), but tuples are *immutable* (strings for instance, are tuples), they're represented by parenthesis:

```py
tuple1 = () # Empty tuple
tuple2 = (1, "hello", 5)

# Examples
tuple2[0]   # Evaluates to 1
tuple2[1:2] # Slice tuple, evaluates to ("hello",) <- extra comma means a tuple with one element
tuple2[1:3] # Slice tuple, evaluates to ("hello", 5)

len(tuple2) # Evaluates to 3
t[1] =  "bye" # Returns an error, you can't modify a tuple
```

They are used to *swap* variable values and when returning *more than one value* from a function, for instance:

```py
def quotientRemainder(x, y):
    quotient = x // y # Integer division
    remainder = x % y
    return (quotient, remainder)

(quot, rem) = quotientRemainder(7, 9) # Receive the values in a tuple
```

```
temp = x
x = y
y = temp

(x, y) = (y, x)
```

#### Manipulating tuples

Tuples can be iterated over, example:

```py
def getData(aTuple):
    nums = ()       # <- Empty tuple
    words = ()
    for t in aTuple:
        nums = nums + (t[0],) # <- Singleton tuple
        if t[1] not in words:
            words = words + (t[1],)
    minN = min(nums)
    maxN = max(nums)
    uniqueWords = len(words)
    return (minN, maxN, uniqueWords)
```

### Lists
