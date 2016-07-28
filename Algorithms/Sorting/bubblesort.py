"""Cormen Implementation"""
a=[4, 7, 2, 3, 1, 1, 0]
for i in range(len(a)-1):
    for j in reversed(range(i+1, len(a))):
        if a[j] < a[j - 1]:
            temp = a[j]
            a[j] = a[j - 1]
            a[j - 1] = temp
print a

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

lst = [5, 7, 3, 4, 1, 9, 10, 0]
bubbleSort(lst)
print lst
