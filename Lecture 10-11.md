# Lecture 10 and 11 - Understanding Program Efficiency

Algorithmic complexity, a rough measure of the efficiency of a program (measuring orders of growth of algorithms). Big “Oh” notation and different complexity classes of algorithms.

## Efficiency of Programs

We started asking the question: How efficient is my algorithm and how can we reason about an algorithm in order to predict the amount of time it will need to solve a problem of a particular size?

- How can we relate choices in algorithm design to the time efficiency of the resulting algorithm? Are there fundamental limits on the amount of time we will need to solve a particular problem?

An algorithm can be implemented in many different ways, but we want to measure the algorithm itself, not the implementation.

We could measure an algorithm complexity by execution time for instance:

Python offers a native timer using the time module:

```py
import time

def CelsiusToFahrenheit(c):
    """ Assumes c is a temperature value measured in Celsius degrees
    Returns the same value converted to Fahrenheit"""
    return c * 9/5 + 32

# Start clock
time0 = time.clock()
CelsiusToFahrenheit(100000)
time1 = time.clock() - time0
print("t =", time0, ":", time1, "s,")
```

But timing is not a good measure because running time varies between: algorithms, implementations, computers. And cant be predictable based on small inputs.

Another method would be counting each steps it performs thru the execution (more abstract). We can start by assuming that **these steps take constant time**: Mathematical Operations, Comparisons, Assignments, Accessing objects in memory, etc. Then we could count the number of operations executed as function of size of inputs.

But also counting operations is not a good measure. Although it's better than timing, it also depends on algorithm, implementation, computer and there are no clear definition of which operations we should count.

To evaluate just the algorithm measuring it's complexity, we can use the abstract notion of **order of growth** (which we can argue is the most appropriate way of asserting the impact of choices of algorithm in solving a problem).

### Big "Oh" Notation - Order of Growth

We want to evaluate the efficiency particularly when the input is very big, expressing the growth of program's run time as input size grows. It does not to be precise, just an "order of growth" will be enough.

By looking at the largest factors in the run time, we can know which section of the program will take the longest to run. **Generally we want a tight upper bound on growth, as function of size of input, in worst case**

**Big Oh (or O())** measures an **upper bound on the asymptotic growth** (order of growth), it's used to describe the worst case:

1. Worst case occurs often and is the bottleneck when a program runs
2. Express rate of growth of program relative to the input size
3. Evaluate the algorithms, not the machine or implementation

**Exact Steps vs O():**

```py
def fact(n):
    """ Assumes n an int >= 0 """
    answer = 1          
    while n > 1:    
        answer *= n
        n -= 1          # temp = n - 1    
                        # n = temp
    return answer
```

Computes Factorial in the iterative way:

    Number of steps: 1 + 5n + 1 = 5n + 2

    Worst case asymptotic complexity: O(n) (grows linearly)
        Ignore additive constants
        Ignore multiplicative constants

**Simplification Examples:** Drop constants and multiplicative factors and focus on **dominant** terms:

1. If the algorithm has for instance $n^2 + 2n + 2$ operations, we say it's O($n^2$) (It's order _n squared_)

2. If the algorithm has $n^2 + 100000n + 3^{1000}$ operations, we say it's O($n^2$)

3. If the algorithm has $\log(n) + n + 4$ operations, we say it's O($n$) (Linear)

4. If the algorithm has $0.0001*n*\log(n) + 300n$ then it's O($n\log(n)$)

5. If the algorithm has $2n^{30} + 3^n$, the it's O($3^n$)

Types of orders of growth are: **Constant, Linear, Quadratic, Logarithmic, $n\log(n)$ and Exponential**

## Analysing Programs and their complexity

We need to combine complexity classes by analysing statements inside functions and focus on dominant term.

**Law of Addition for O()**

1. Used with **sequential statements:**
    O(f(n)) + O(g(n)) is equal to O(f(n) + g(n)). Example:

```py
for i in range(n): # O(n)
    print('a')
    for j in range(n*n): # O(n * n)
        print('b')
```

In the first case ```for i in range(n)``` it's linear in size of n, then O($n$). For the second case ```for j in range(n*n)``` it's squared O($n^2$), so the addition will be: O($n$) + O($n^2$) = O($n+n^2$) = O($n^2$) because of the dominant term $n^2$. **Nested loops** are O($n^2$).

**Law of Multiplication for O()**
1. Used with **nested statements/nested loops**
O(f(n)) * O(g(n)) is equal to O(f(n) * g(n)). Example:

```py
for i in range(n): # O(n)
    for j in range(n): # O(n)
        print('a')
```

Will be: O($n$) * O($n$) = O($n*n$) = O($n^2$) because the outer loop goes $n$ times and the inner loop goes $n$ times for every outer loop iteration. Nested loops typically have this behaviour.

**Complexity Classes**

1. O($1$) denotes constant running time: The amount of time doesn't depend on the size of the problem. They're very rare.

2. O($\log n$) denotes logarithmic running time:

3. O($n$) denotes linear running time:

4. O($n \log n$) denotes log-linear running time:

5. O($n^c$) denotes polynomial running time (where c is a constant)

6. O($c^n$) denotes exponential running time (c is a constant being raised to power based on size of input)

### Linear Complexity

Simple iterative loop algorithms are typically linear in complexity. For instance, a **linear search on an unsorted list**:

```py
def linearSearch(list, element):
    """ Assumes a list (unsorted) and the element being searched
    Returns tif the element is found or not """
    found = False
    for i in range(len(list)):  # O(len(list))
        if element == list[i]:  # O(1)
            found = True # Returning true here would not make a difference for the overall complexity. It would stop the program faster
    
    return found
```

In the above example, the algorithm must look thru all the elements of a list to decide it's not there. The O(len(list)) for the loop * O(1) to test if element is list[i] (This is assuming that we can retrieve the element of a list in a constant time). So O($1 + 4n + 1$) = O($4n+2$) = O($n$) (the overall complexity) where $n$ is len(list).

**Linear search on a sorted list**

```py
def search(list, element):
    """ Assumes a list (sorted) and the element being searched
    Returns tif the element is found or not """
    for i in range(len(list)): # O(len(list))

        if list[i] == element: # O(1)
            return True
        if list[i] > e:
            return False
        
    return False
```

In the above example it must only look until reach a number greater than the element, so O(len(list)) for the loop * O(1) to test if element is list[i]. So the overall complexity is O($n$). The order of growth will be the same as for an unsorted list, but the run time might differ for each search method.

### Quadratic Complexity

Nested iterative loop algorithms are typically quadratic in complexity. For instance, determine if a list is a subset of a second:

```py
def isSubset(list1, list2):
    """ Assumes two lists and verify if each element of list1 also appears in list2 (assumes no duplicates)"""
    for element1 in list1: # O(len(list1))
        matched = False
        for element2 in list2: # O(len(list2))
            if element1 == element2: # O(1)
                matched True
                break
        if not matched: # O(1)
            return False
    
    return True
```

The first loop ```for element1 in list1``` is executed len(list1) times, as ```for element2 in list2``` will be executed up to len(list2) times, with constant numbers of operations (If). So we have a case of **Multiplication for O()**, which will be O(len(list1)) * O(len(list2)). Worst cases are: when L1 and L2 are the same size or none of elements in List1 are in List2. Then the overall complexity will be: O(len(list1)$^2$)

Another example, to find the intersection of two lists and return a list with each element appearing only once:

```py
def intersection(list1, list2):
    """ Assumes two lists and verify if each element of list1 also appears in list2 (only once). Returns the intersection of the elements"""
    temp = []
    for element1 in list1: # O(len(list1))
        for element2 in list2: # O(len(list2))
            if element1 == element2: # O(1)
                temp.append(element1)
    
    res = []
    for element in temp # O(len(temp))
        if not(element in res)
            res.append(element)

    return res
```

Worst case scenario: all elements of list1 and list2 are the same, so len(temp) will be len(list1), thus (O(len(list1)) * O(len(list2))) will be equal to O(len(list1)$^2$), O(len(list1)$^2$) * O(len(list1)) = O(len(list1)$^2$).

**O() for nested loops**

```py
def g(n):
    """ Assumes n >= 0 """
    x = 0
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            x +=1
    
    return x
```

Computes $n^2$ very inefficiently. When dealing with nested loop, look at the ranges. In this case each nested loops is iterating n times, so O($n^2$)

### Constant Complexity

The asymptotic complexity is independent of the size of the inputs. For instance: finding the length of a list, multiplying two numbers, assigning a value to a variable.

### Logarithmic Complexity O($\log n$)

In logarithm complexity we don't cre about the base of the log, but we want to analyze a function that grows as the log of at least one of the inputs. One example is Binary Search.

An algorithm with log complexity:

```py
def intToStr(i):
    """ Assumes I is nonnegative integer
    Returns a decimal string representation of i"""
    digits = '0123456789'

    if i == 0:
        return '0'

    result = ''

    while i > 0:
        result = digits[i%10] + result
        i = i // 10

    return result
```

We can check that there are no function or method calls in this piece of code, we know that we only have to look at the loops to determine the complexity class. Since there's only one loop, we only need to characterize the **number of iterations**. So it's the number of times we can use integer division to divide i by 10 before getting a result of 0. So the result of ```intToStr``` is O($\log (i)$).

Check the complexity of ```addDigits```:

```py
def addDigits(n):
    """ Assumes n is a nonnegative integer
    Returns the sum of the digits in n"""
    stringRep = intToStr(n)

    val = 0

    for c in stringRep:
        val += int(c)
    
    return val
```

When running ```addDigits```, we are calling ```intToStr``` which has a complexity of O($log(i)$). But for the loop we are calling inside ```addDigits``` will be executed O($n$) times, where $n$ is the size of ```stringRep```. This program will run in time proportional to O($\log(n)$) + O($\log(n)$), which makes it O($\log(n)$)

### Log-Linear Complexity

This one is more complicated than the complexity we've looked so far, so we will skip it for now.

### Polynomial Complexity

It's similar as **quadratic complexity**, but let's consider the following function:

```py
def isSubset(L1, L2):
    """ Assumes L1 and L2 are lists
    Returns True if each element in L1 is also in L2 (L1 is a subset of L2), False otherwise"""

    for element1 in L1:
        matched = False

        for element2 in L2:
            if element1 == element2:
                matched = True
                break # Attention to the usage of break in Python
        
        if not matched:
            return False
        
    return True
```

Note that we are doing a nested for, for L1 and also for L2. The inner loop is executed O(len(L2)) times, and the outer loop is executed O(len(L1)) times. Thus the complexity of this function is O(len(L1) * len(L2)).

Now let's take a look on another function:

```py
def intersect(L1, L2):
    """ Assumes L1 and L2 are lists
    Returns the Intersection of the two lists """

    # Build a list containing common elements
    temp = []

    for element1 in L1:

        for element2 in L2:
            if element1 == element2:
                temp.append(element1)
                break
        
    # Build the intersection: no duplicated items (if any)
    intersection = []

    for element in temp:
        if element not in intersection:
            intersection.append(element)

    return intersection
```

Since the lengths of ```intersection``` and ```temp``` are bounded by the length of the smaller of L1 and L2, the complexity of intersect is O(len(L1) * len(L2))

### Exponential Complexity

We'll check that later, but many important problems are inherently exponential. The knapsack is one of these problems were solving them completely can require time that is exponential in the size of the input (For instance, when we have 6 choices to put in the knapsack, the complexity can have O($2^n$)). Consider the following code:

```py
def powerSet(L):
    """ Assumes L is a list
    Return a list of lists that contains all possible combinations of elements of L (powerset of L)"""

    powerSet = []
    for i in range(0, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []

        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])

        powerSet.append(subset)
    
    return powerSet
```

Remember the property of a powerset that states:

- If a set has $n$ elements, its power set will contain $2^n$ subsets.

We're using ```getBinaryRep``` to represent any combination of elements by a string of n 0 and 1, where 1 represents the presence of an element and 0 its absence. This, generating all subsets of a set L of length n can be done in the following way:

1. Generate all n-bit binary numbers. These are the numbers from 0 to $2^n$

2. For each of these $2^n + 1$ binary numbers, generate a list by selecting elements of L that have an index corresponding to a 1 in binary. For instance, if L is [1, 2] and the binary representation is 01, then generate the list [2].

If we try to generate the power set of a set containing 10 elements, it will produce a list of $2^{10} = 1024$ elements. But what if we want to run with a larger set, we can check the algorithm will take longer to run. Thus we reach a point where this algorithm becomes inefficient, because it is **inherently exponential**. This mean we should find algorithms that find approximations to these kind of problems, or some can find perfect solutions on some instances of the problem.