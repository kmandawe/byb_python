from inheritance_example import SortedIntList, SortedList, IntList

print(SortedIntList.mro())

print(super(SortedList, SortedIntList))

print(super(SortedList, SortedIntList).add)

# print(super(SortedList, SortedIntList).add(4))

print(super(SortedIntList, SortedIntList)._validate(5))
# print(super(SortedIntList, SortedIntList)._validate('hello'))

# super(int, IntList)

