def union(L1, L2):
    """ Assumes L1 and L2 are lists
    Returns the Union of the two lists"""

    #Builds a list containing all elements in L1
    union = L1

    # Now append every element of L2 in the union set
    for element2 in L2:

        if element2 not in union:
            union.append(element2)

    return union

def intersection(L1, L2):
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

    
def setMinus(L1, L2):
    """ Assumes L1 and L2 are lists
    Returns L1 \ L2 which is everything that's L1 but not in L2"""
    minusSet = []

    for element1 in L1:
        if element1 not in L2:
            minusSet.append(element1)

    return minusSet

def complement(L1, L2):
    """ Assumes L1 and L2 are lists and L1 is the universal set
    Returns the complement of L2 in L1"""
    complement = []

    for element1 in L1:

        if element1 not in L2:
            complement.append(element1)

    return complement

def isElement(element, L1):
    """ Assumes element is a number, L1 is a list
    Returns True if element is in L1, False otherwise """

    if element in L1:
        return True
    else:
        return False
    
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

def getBinaryRep(n, numDigits):
    """ Assumes n and numDigits are nonnegative integers
    Returns a string of length numDigts that is a binary representation of n"""
    result = ''

    while n > 0:
        result = str(n % 2) + result
        n = n // 2

    if len(result) > numDigits:
        raise ValueError('not enought digits')
    
    for i in range(numDigits - len(result)):
        result = '0' + result

    return result

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


# Testing...

# Some sets for test
L1 = [2, 4, 6, 8, 10]
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L3 = [1, 2, 3]
L4 = [3, 4, 5, 6]

L5 = [1, 2, 3, 4, 5]
L6 = [1, 2]



print(f"Is L1 a subset of L2? {isSubset(L1, L2)}")
print(f"{L1} ∩ {L2} = {intersection(L1, L2)}")
print(f"{L3} ∪ {L4} = {union(L3, L4)}")
print(f"{L3} \ {L4} = {setMinus(L3, L4)}")

print(f"The complement of {L6} in {L5} is {complement(L5,L6)}")

print(f"Is 3 an element of {L4}? {isElement(3, L4)}")
print(f"Is 3.14 an element of {L4}? {isElement(3.14, L4)}")

print(f"The powerset P({L3}) = {powerSet(L3)}")