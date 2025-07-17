def getData(aTuple):
    """
    aTuple is a tuple of tuples with elements (int, string)
    Extracts all integers from aTuple and sets
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    nums = ()       # <- It will create two empty tuples, nums and words
    words = ()      # <- second empty tuple words

    # Iterating over tuple objects
    for t in aTuple:
        nums = nums + (t[0],) # <- Singleton tuple (tuple of one element)
        if t[1] not in words:
            words = words + (t[1],)
    minNums = min(nums)
    maxNums = max(nums)
    uniqueWords = len(words)
    return (minNums, maxNums, uniqueWords)

# Cars
hondaCars = ((1990, "Honda NSX"),
             (1992, "Honda CR-X"),
             (1992, "Honda Prelude 4th gen"),
             (1994, "Honda Odyssey"),
             (1995, "Honda CR-V 1th gen"),
             (1996, "Honda Civic 6th gen"),
             (1997, "Honda Civic Type R"),
             (1998, "Honda HR-V 1th gen"),
             (1999, "Honda S2000"))

(minYear, maxYear, numCars) = getData(hondaCars)

print("From", minYear, "to", maxYear, \
      "Honda launched", numCars, "different car models!")