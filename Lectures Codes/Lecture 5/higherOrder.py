def applyToEach(list, function):
    """
    Assumes list is a list, function is a function
    It mutates list by replacing each element e of list by function(e)
    """
    for i in range(len(list)):
        list[i] = function(list[i])

list1 = [1, -2, 3.33]

# Original List
print("List1 = ", list1)

#Apply abs() to each element of list1
applyToEach(list1, abs)
print("list1.abs():", list1)

#Cast everything to int:
applyToEach(list1, int)

print("List 1 as int: ", list1)
