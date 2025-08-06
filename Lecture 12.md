# Lecture 12 - Searching and Sorting

Introduction to Algorithms: Search and Sorting algorithms are the most important algorithms, in this lecture we will learn about linear search, bisection search, bubble sort, selection sort and merge sort.

## Search Algorithms - Recap

A way to find an item (or group of items) from a collection (implicit or explicit). We have already used some algorithms for searching like the bisection implementation to find an square root. In this example the collection was **implicit** (some numbers in between a start and end point).

Search algorithms were the collection is **explicit**, for instance all the data record from student, how to find an specific student name? 


**Search over an list of numbers**

    Linear search:
        - Brute force search (British Museum Algorithm or Exhausted Enumeration)
        - List does not have to be sorted

    Bisection Search:
        - List must be sorted to give correct answer
        - We've already seen two different implementations of it

Linear search, the worst case is the element is not in the list. Example:

```py
def linearSearch(unsortedList, element):
    found = False
    for i in range(len(unsortedList)):
        if element == unsortedList[i]:
            found = True
        
    return found
```

Where O(len(unsortedList)) for the loop * O(1) to test ```if element == unsortedList[i]```. So overall complexity is O(n).

Linear search on a **sorted list**:

```py
def search(sortedList, element):
    for i in range(len(sortedList)):
        if sortedList[i] == element:
            return True
        if sortedList[i] > element
            return True

    return False
```

**Bisection Search**:

```py
def bisectionSearch(sortedList, element):
    def bisectionSearchHelper(sortedList, element, low, high):
        if high == low:
            return sortedList[low] == element
        
        mid = (low + high) // 2

        if sortedList[mid] == element:
            return True
        
        elif sortedList[mid] > element:

            if low == mid: # When there's nothing else left to search
                return False

            else:
                return bisection_search_helper(sortedList, element, low, mid - 1)  

        else:
            return bisection_search_helper(sortedList, element, mid + 1, high)   

    if len(sortedList) == 0
        return False

    else:
        bisection_search_helper(sortedList, element, 0, len(sortedList) - 1)
```

When does it make sense to sort the list and then do the search? Searching a sorted list: (n is the list's length):

    - Using linear search, search for an element is O(n)

    - Using binary search, can search for an element in O(log n) (assuming the list is sorted)


So, when does it make sense to **sort first then search**?

    - SORT + O(log n) < O(n) → SORT < O(n) - O(log n)

    - When sorting is less than O(n)

**Amortized cost (n is len(list))**

Sorting first in some cases then do many searches **amortizes the cost** of the sort over many searches (K searches):

    SORT + K * O(log n) < K * O(n)
        → For large K, sort time becomes irrelevant if cost of sorting is small enough

## Sorting Algorithms

- **Monkey sort** 

    - Or bogosort, stupid sort, slowsort, permutation sort, shotgun sort
    
    - Randomly sorting a list exhaustively 

```py
def bogoSort(L):
    while not is_sorted(L):
        random.shuffle(L)
```

Best case: O(n) where n is len(L) to check if sorted, worst case: O(?)

---

- **Bubble Sort**

    - **Compare** consecutive pairs of elements

    - **Swap elements** in pair such that smaller is first

    - When reach **end of the list**, start all over again

    - Stops when **no more swaps** have been made

    - Largest unsorted element always at end after pass, so at most n passes

```py
def bubbleSort(L):
    swap = False

    while not swap: # O(len(L))

        swap = True

        for j in range(1, len(L)): # O(len(L))

            if L[j - 1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = temp
```

- Complexity of bubble sort:
    - Inner for loop is for doing the comparisons

    - Outer while loops is for doing multiple passes until no more swaps

    - O($n^2$) where n is len(L)

---

- **Selection Sort**

    - First Step:
        - Extract **minimum element**

        - **Swap it** with element at **index 0**

    - Subsequent Steps:
        - In remaining sublist, extract **minimum element**

        - **Swap it** with the element at **index 1**

    - Keep the left portion of the list sorted:
        - At the i`th step, **first i elements in list are sorted**

        - All other elements are bigger than first i elements

**Analyzing Selection sort**
- Loop invariant

    Given prefix of list L[0:i] and suffix L[i + i: len(L)], then prefix is sorted and no element in prefix is larger than smallest element in suffix

    1. Base case: prefix empty, suffix whole list - invariant true

    2. Induction Step: move minimum element from suffix to end of prefix. Since invariant True before move, prefix sorted after append

    3. When exit, prefix is entire list, suffix empty. Therefore, sorted


```py
def selectionSort(L):
    suffixStarter = 0

    while suffixStarter != len(L): # len(L) times, O(len(L))

        for i in range(suffixStarter, len(L)): # len(L) - suffix times, O(len(L))

            if L[i] < L[suffixStarter]:
                L[suffixStarter], L[i] = L[i], L[suffixStarter]

        suffixStarter += 1
```

- Complexity of **selection sort**:

    - Outer loop executes len(l) times

    - Inner loop executes len(l) - i times

    - Complexity of selection sort is O($n^2$)

---

- **Merge Sort**

    - Divide and conquer

    - 

```py
def merge(left, right):

    result = []
    i, j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while (i < len(left)):
        result.append(left[i])
        i += 1

    while (j < len(right)):
        result.append(right[j])
        j += 1
    
    return result

def mergeSort(L):
    
    if len(L) < 2: # Base case
        return L[:]
    
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])

        return merge(left, right)

```

- Complexity of merging sublists step

    - go thru two lists, only one pass

    - compare only **smallest elements in each sublist**

    - O(len(left) + len(right)) copied elements

    - O(len(longer list)) comparisons

    - **Linear in length of the lists**

- Complexity of Merge Sort (Recursive)

    - Divide list successively into halves

    - depth-first such that **conquer smallest pieces down one branch** first before moving to larger pieces
