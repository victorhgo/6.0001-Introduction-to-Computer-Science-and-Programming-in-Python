def removeDups(list1,list2):
    """
    Assumes that list1 and l2 are lists.
    Removes any element from List1 that also occurs in list2
    """
    for element in list1:
        if element in list2:
            list1.remove(element)

def removeDupsSlicing(list1,list2):
    """
    Assumes that list1 and l2 are lists.
    Removes any element from List1 that also occurs in list2
    """
    for element in list1[:]:
        if element in list2:
            list1[:].remove(element)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 3, 5, 7, 9]

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l4 = [2, 4, 6, 8, 10]

# Will remove all odds from L1
removeDups(l1,l2)

# Will remove all evens from L3
removeDups(l3,l4)

print("l1 =", l1)
print("l3 =", l3)

# We can clone a list to avoid editing the main list, by running the second function:
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 3, 5, 7, 9]

# It will not affect the list1
l5 = removeDupsSlicing(l1, l2)

print("List1[:] = ", l1)
print("List5: ", l5)