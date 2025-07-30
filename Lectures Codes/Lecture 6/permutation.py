"""
Exercise 18 -  Write a recursive function to print all permutations of a string. (Part of Pset4)

Comments:

As an example, the string ABC has 6 permutations: ABC, ACB, BAC, BCA, CBA and CAB. """

# First we need to take a string and return it as a list of characters. Eg: input string 'ABC' returns '['A', 'B', 'C']
def toList(string):
    """
    Assumes string is an string
    Returns a list of characters from string
    """
    lst = []
    for element in string:
        lst.append(element)
    
    return lst