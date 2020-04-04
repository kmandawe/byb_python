from timeit import timeit
timeit(setup="from __main__ import resolve", stmt="resolve('python.org')", number=1)
