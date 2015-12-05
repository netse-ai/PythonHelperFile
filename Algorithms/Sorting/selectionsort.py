def selectionSort(alist):
    for index in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, index+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[index]
        alist[index] = alist[positionOfMax]
        alist[positionOfMax] = temp
    print alist

testlist = [1, 4, 2, 5, 3, 6, 7, 9, 8]
selectionSort(testlist)
