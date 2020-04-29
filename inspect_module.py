import inspect
import sorted_set


print(inspect.ismodule(sorted_set))
# print(inspect.getmembers(sorted_set))
print(dir(inspect))
print(inspect.getmembers(sorted_set, inspect.isclass))

from sorted_set import chain
print(list(chain([1, 2, 3], [4, 5, 6])))

print(inspect.getmembers(sorted_set.SortedSet, inspect.isfunction))

init_sig = inspect.signature(sorted_set.SortedSet.__init__)
print(init_sig)
print(init_sig.parameters)
print(repr(init_sig.parameters['items'].default))
print(str(init_sig))
print(inspect.signature(abs))