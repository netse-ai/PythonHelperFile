def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current = alist[i]
        position = i

        while position > 0 and alist[position-gap] > current:
            alist[position] = alist[position-gap]
            position -= gap

        alist[position] = current

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
