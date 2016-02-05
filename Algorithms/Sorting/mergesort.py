import random
import os

merge = random.sample(range(100000),100000)

def merge_sort(alist):
    """ Merge Sort is a recursive sorting algorithm.  It is designed to split a list into
    in half (left and right) until values are in their own discrete list. Comaprisons are
    made at every call to determine which values are greater than or less than. When the
    algorithm reaches the point in which the values are in discrete lists, comparisons
    are made to determine which values are swapped.

    This algorithm requires more space than the usual sorting algorithm because it makes
    2 lists (left and right) in equal size to the original list, which is of size 'n'. When
    the recursive calls are made, the operations are 'n/2', or 'log2(n)'.

    As a result, we get T(n) = n(log(n)) or O(n(log(n))."""

    if len(alist) > 1:
        mid = len(alist) // 2
        right = alist[mid:]
        left = alist[:mid]

        i = 0
        j = 0
        k = 0

        merge_sort(right)
        merge_sort(left)

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

    return alist

print merge_sort(merge)
