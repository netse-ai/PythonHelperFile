import time
import random
from functools import wraps

radix = random.sample(range(10000),10000)

adpmerge = random.sample(range(10000),10000)

merge = random.sample(range(10000),10000)

insertion = random.sample(range(100),100)

selection = random.sample(range(100),100)

bubble = random.sample(range(100),100)


def fn_timer(function):
    """Function for timing other functions"""
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (function.func_name, str(t1-t0))
               )
        return result
    return function_timer

@fn_timer
def selectionSort(alist):
    """ 0.053111076355 seconds"""
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp



@fn_timer
def insertionSort(alist):
    """0.0537369251251 seconds"""
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = currentvalue



@fn_timer
def adaptiveMergeSort(alist):
    """0.000439882278442 seconds"""
    alist.sort()


@fn_timer
def merge_timer(alist):
    def merge_sort(alist):
        if len(alist)>1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            merge_sort(lefthalf)
            merge_sort(righthalf)

            i = 0
            j = 0
            k = 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i += 1
                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1


@fn_timer
def radix_sort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in random_list:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_random_list:
            return new_list[0]

        random_list = []
        rd_list_append = random_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)


def test(r, s, m, a, i):
    radix_sort(r)
    insertionSort(i)
    selectionSort(s)
    merge_timer(m)
    adaptiveMergeSort(a)

test(radix, selection, merge, adpmerge, insertion)
