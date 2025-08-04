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
    """
    Assumes c is temperature measured in Celsius degrees
    Converts it to Fahrenheit """
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

- Number of steps: 1 + 5n + 1 = 5n + 2

- Worst case asymptotic complexity: O(n) (grows linearly)
  Ignore additive constants
  Ignore multiplicative constants

**Simplification Examples:** Drop constants and multiplicative factors and focus on **dominant** terms:

If the algorithm has for instance $n^2 + 2n + 2$ operations, we say it's O($n^2$) (It's order _n squared_)

If the algorithm has $n^2 + 100000n + 3^{1000}$ operations, we say it's O($n^2$)

If the algorithm has $\log(n) + n + 4$ operations, we say it's O($n$) (Linear)

If the algorithm has $0.0001*n*\log(n) + 300n$ then it's O($n\log(n)$)

If the algorithm has $2n^{30} + 3^n$, the it's O($3^n$)

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

In the first case ```for i in range(n)``` it's linear in size of n, then O($n$). For the second case ```for j in range(n*n)``` it's squared O($n^2$), so the addition will be: O($n$) + O($n^2$) = O($n+n^2$) = O($n^2$) because of the dominant term $n^2$

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

### Logarithmic Complexity


### Polynomial Complexity


### Exponential Complexity