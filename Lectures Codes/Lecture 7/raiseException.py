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

