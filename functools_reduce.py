from functools import reduce

import operator

reduced = reduce(operator.add, [1, 2, 3, 4, 5])

print(reduced)

numbers = [1, 2, 3, 4, 5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator, item)

print(accumulator)


def mul(x, y):
    print('mul {} {}'.format(x, y))
    return x * y


reduced = reduce(mul, range(1, 10))
print(reduced)

# reduce(mul, [])
print(reduce(mul, [1]))

values = [1, 2, 3]
print(reduce(operator.add, values, 0))

values = []
print(reduce(operator.add, values, 0))

values = [1, 2, 3]
reduced = reduce(operator.add, values, 0)
print(reduced)

reduced = reduce(operator.mul, values, 1)
print(reduced)
