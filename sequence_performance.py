from sorted_set import SortedSet
from random import randrange

s = SortedSet(randrange(1000) for _ in range(2000))
print(s)
print(len(s))

print([s.count(i) for i in range(1000)])


from timeit import timeit
print(timeit(setup='from __main__ import s',
       stmt='[s.count(i) for i in range(1000)]',
       number=100))
