""" Binary search: Suppose L an ordered list, if we want to check if element is in L:
1 - Take len(L) divides in half, check if L[half] == element
2 - If not, check whether L[half] is greater or smaller than e
    - If smaller, check the half on the right
    - If greater, check the half on the left

3 - Do that until find e or not

First I'll write a small function to sort the elements of L to ensure they're in ascending order
"""
import random 

def search(L, e):
    """ Assumes L is a sorted list of positive integers and e is the element we want to check if in L
        Returns True if element is found, False otherwise"""
    
    # We'll call it recursively
    def binarySearch(L, e, low, high):
        """ Base case, if high = low means we have "sliced" 
        the list to a point where there's no more way to slice it """
        if high == low:
            # True if element is L[low], false otherwise
            return L[low] == e

        middle = (low + high) // 2

        # "Slice" the list and check if element is L[middle]
        if L[middle] == e:
            return True
        
        # If element L[middle] is greater than element, we search the left half of the list
        elif L[middle] > e:
            # There's nothing else to search
            if low == middle:
                    return False
            else:
                return binarySearch(L, e, low, middle - 1)
            
        # If element L[middle] is smaller than element, we search the right half of the list
        else:
            return binarySearch(L, e, middle + 1, high)
        
    # Empty list, nothing to search for
    if len(L) == 0:
        return False 
    else:
        return binarySearch(L, e, 0, len(L) - 1)

# Builds a large list of integers to test the runtime for this algorithm (based on input n)
def buildList(m, n):
    """ Assumes n is a positive integer
        Returns a list of size n containing all positive integers from m to n """
    L = []

    for i in range(m, n):
        L.append(i)

    return L
    
# Test 1
list1 = [1, 2, 3, 4, 5, 6]
e = 4

print(search(list1, e))

# Test 2: big list 1 to 100
list2 = buildList(1, 100)

print(search(list2, 99))

# Test 3: a list of words - it won't work for a list of strings because binary search only works for ordered lists
# where the elements are integers

list3 = ['hello', 'victor', 'peanut', 'echo', 'november', 'alfa']
element = 'alfa'

print(search(list3, element))

# Test 4 - A list of numbers but negative
list4 = buildList(-50, 50)
print(search(list4, -25))

# It also work for finding negative numbers

# Finding a random number
list5 = buildList(-100, 100)
i = random(100)
print(search(list5, i))

