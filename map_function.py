new_val = map(ord, "The quick brown fox")
print(new_val)

from instances_decorator import Trace

result = map(Trace()(ord), "The quick brown fox")

print("RESULT:")
print(result)
print(next(result))
print(next(result))
print(next(result))

print("CREATING LIST")
l = list(map(ord, "The quick brown fox"))
print(l)

for o in map(ord, "The quick brown fox"):
    print(o)
