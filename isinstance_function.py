from inheritance_example import SortedList, SimpleList

print(isinstance(3, int))
print(isinstance('hello!', str))

print(isinstance(4.567, bytes))
sl = SortedList()
print(isinstance(sl, SortedList))
print(isinstance(sl, SimpleList))

x = []
print(isinstance(x, (float, dict, list)))

