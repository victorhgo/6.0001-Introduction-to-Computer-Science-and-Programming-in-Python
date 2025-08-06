def bubbleSort(L):
    swap = False
    while not swap:
        print("Bubble sorting:", L)
        swap = True
        for j in range(1, len(L)):

            if L[j - 1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j - 1]
                L[j - 1] = temp

testList = [1, 3, 5, 6, 2, 25, 18, 17, 13]

print("Before sorting:", testList,'\n')

bubbleSort(testList)

print("\nAfter sorting:", testList)
