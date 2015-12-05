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

"""Implementation of fn_timer()"""
@fn_timer
def random_sort(n):
    return sorted([random.random() for i in range(n)])


if __name__ == "__main__":
  random_sort(2000000)
