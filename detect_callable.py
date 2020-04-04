def is_even(x):
    return x % 2 == 0


print(callable(is_even))

is_odd = lambda x: x % 2 == 1
print(callable(is_odd))
print(callable(list))
print(callable(list.append))


class CallMe:
    def __call__(self):
        print("Called!")


call_me = CallMe()
print(callable(call_me))

print(callable("This is not callable"))
