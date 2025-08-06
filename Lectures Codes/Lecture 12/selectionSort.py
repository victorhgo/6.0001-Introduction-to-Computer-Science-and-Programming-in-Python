def selectionSort(L):
    suffixStarter = 0

    while suffixStarter != len(L):
        print('Sorting...', L)
        for i in range(suffixStarter, len(L)):
            
            if L[i] < L[suffixStarter]:
                L[suffixStarter], L[i] = L[i], L[suffixStarter]
                

        suffixStarter += 1

testList = [1, 3, 5, 6, 2, 25, 18, 17, 13]

print("Before sorting:", testList,'\n')

selectionSort(testList)

print("\nAfter sorting:", testList)

