import time
import random
from functools import wraps

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

numbers = random.sample(range(1000),1000)

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

# selectionSort(numbers)


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

# insertionSort(numbers)

@fn_timer
def adaptiveMergeSort(alist):
    """0.000439882278442 seconds"""
    numbers.sort()
# adaptiveMergeSort(numbers)
