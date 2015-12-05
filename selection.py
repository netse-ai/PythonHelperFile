def selectionSort(alist):
    for i in range(len(alist)-1, 0, -1):
        maxpos = 0
        for j in range(1, i+1):
            if alist[j] > alist[maxpos]:
                maxpos = j
        temp = alist[i]
        alist[i] = alist[maxpos]
        alist[maxpos] = temp

testlist = [3, 2, 1, 5, 6, 87, 7]
selectionSort(testlist)
print testlist
