def merge(left, right):
    result = []
    i, j = 0,0

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
    
    print("Merge:", left, '&', right, 'to', result)
    return result

def mergeSort(L):
    print('Merge sorting...', L)
    if len(L) < 2:
        return L[:]
    
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])

        return merge(left, right)
    
testList = [1, 3, 5, 6, 2, 25, 18, 17, 13]

print("Before sorting:", testList,'\n')

mergeSort(testList)

print("\nAfter sorting:", testList)