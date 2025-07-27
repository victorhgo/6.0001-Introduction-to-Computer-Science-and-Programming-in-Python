"""
Exercise 18 -  Write a recursive function to print all permutations of a string. (Part of Pset4)

Comments:

As an example, the string ABC has 6 permutations: ABC, ACB, BAC, BCA, CBA and CAB. Python offers a native solution for that:

permutations(p[, r]) function from lib itertools () (itertools - Functional tools for creating and using iterators.):

Help on class permutations in module itertools:

class permutations(builtins.object)
 |  permutations(iterable, r=None)
 |
 |  Return successive r-length permutations of elements in the iterable.
 |
 |  permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)

----------------------------------------------
"""

# Example with permutations (Python native):
import itertools

string = 'ABC'

# Put string into a list of chars:
list1 = list(string)
print("List1:", list1)
# Put every permutation of list1 into a list permut: if list1 = ['A', 'B', 'C'], then permuts = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'] (not formatted as list)
permut = list(itertools.permutations(list1))

print("Permut =", permut)

# Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
print([''.join(permutation) for permutation in permut])

# Iterative one:
def Permutation(string):
    """
    Receives an string
    Returns all permutations of string
    """
    if not string: # Base case, if string is empty
        return []