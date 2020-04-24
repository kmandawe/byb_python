from inheritance_example import SimpleList, SortedList, IntList

print(issubclass(IntList, SimpleList))
print(issubclass(SortedList, IntList))


class MyInt(int): pass


class MyVerySpecialInt(MyInt): pass


print(issubclass(MyVerySpecialInt, int))