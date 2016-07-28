import timeit

list_index = timeit.Timer("x[5]", "from __main__ import x")

x = list(range(20000))
list_index.timeit(number=55)
