from inheritance_example import *

from pprint import pprint as pp

pp(SortedIntList.mro())

sil = SortedIntList([5, 15, 10])
pp(sil)

print(super(SortedList, sil))

print(super(SortedList, sil).add(6))

pp(sil)

super(SortedList, sil).add('I am not a number! I am a free man!')

pp(sil)