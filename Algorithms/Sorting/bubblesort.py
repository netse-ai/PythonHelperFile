def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print alist
bubbleSort(alist)
print alist


"""Short bubble sort"""
def ShortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                temp = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

newlist = [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
ShortBubbleSort(newlist)
print newlist
