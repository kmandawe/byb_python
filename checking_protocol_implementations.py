from collections.abc import *

print(issubclass(list, Sequence))

print(issubclass(list, Sized))

print(issubclass(dict, Mapping))

print(issubclass(dict, Sized))

print(issubclass(dict, Iterable))

