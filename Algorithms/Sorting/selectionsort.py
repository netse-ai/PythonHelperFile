def selectionSort(alist):
    for i in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for j in range(1, i+1):
            if alist[j] > alist[positionOfMax]:
                positionOfMax = j

        temp = alist[i]
        alist[i] = alist[positionOfMax]
        alist[positionOfMax] = temp

lst = [4, 1, 0, 22, 34, 21]
selectionSort(lst)
print lst
