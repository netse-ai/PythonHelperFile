"""The insertion sort list works by starting at an index
and through each pass, it moves from item 1 to item n-1, checking the current
item versus the already sorted sublist.  Items with greater value in the sublist
are moved to the right if they have a higher value, while lower valued items are
on the left. The current item is then inserted into the gap.  This algorithm
takes O(n**2) time."""

def insertionSort(alist):
    """Takes a list as a positional argument"""
    for index in range(1, len(alist)):
        """iterates through the list, assigning currentvalue as the current
        index"""
        currentvalue = alist[index]
        position = index
        """If the position is greater than 0 or the index - 1 is less than
        current value, the position is then assigned to index - 1. The position
        is then lowered a value.  That position then becomes currentvalue oustide
        of the while loop."""
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue

alist = [30, 200, 55, 2, 899, 100, 5]
insertionSort(alist)
print alist
