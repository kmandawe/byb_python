from inheritance_example import *

print(IntList.mro())

print(SortedIntList.mro())

print(list.mro())

print(int.mro())


class NoBaseClass: pass


print(NoBaseClass.__bases__)

print(dir(object))