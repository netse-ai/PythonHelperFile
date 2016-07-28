"""The sequential search goes through an algorithm in a linear, or
'sequential' way.  It goes through the list until the value is found, one by one.
When the value is found, it stops.
"""
def sequentialSearch(unsortedlist, item):
    pos = 0
    found = False

    while pos < len(unsortedlist) and not found:
        if unsortedlist[pos] == item:
            found = True
        else:
            pos += 1

    return found
unsortedlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print sequentialSearch(unsortedlist, 3)
print unsortedlist
print sequentialSearch(unsortedlist, 13)
print unsortedlist

#
"""This is the same algorithm implemented with a sorted list.  If the value does
not exist in the sorted list, it stops when the value above the nonexistent
one is found."""

def unsortedSequentialSearch(orderedlist, item):
    pos = 0
    found = True
    while pos < len(orderedlist) and not found:
        if orderedlist[pos] == item:
            found = True
        else:
            pos += 1
    return found

orderedlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print sequentialSearch(unsortedlist, 3)
print unsortedlist
print sequentialSearch(unsortedlist, 13)
print unsortedlist
