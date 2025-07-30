def getRatios(list1, list2):
    """
    Assumes list1 and list2 are lists of equal length of numbers
    Returns a list containing list1[i]/list2[i] 
    """
    ratios = []
    for index in range(len(list1)):
        try:
            ratios.append(list1[index]/list2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan = not a number
        except:
            raise ValueError("getRatios called with bad arg")
        
    return ratios

def test():
    """
    Let's put some arbitrary values in list1 and list2 to test the getRatios function and also the exceptions
    Tests to be done:
        - When lists are different length
        - When lists have different types
        - When lists are empty
        - When another type is passed to list
    """
    list1 = ['a', 'b', 1, 2]
    list2 = ['hello', 50.35, None, False]
    #print("Test1, different types", getRatios(list1, list2))

    list3 = [1, 2, 3]
    list4 = [4, 5, 6]
    print("Test2, same types (ints):", getRatios(list3, list4))

    list6 = [2.8, 3.6, 4.9]
    list5 = [44, 21.5, 3.77]
    print("Test3, different types(floats and integers):", getRatios(list5, list6))

test()