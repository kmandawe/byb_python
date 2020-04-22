vals = [[y * 3 for y in range(x)] for x in range(10)]
print(vals)

set_vals = {x * y for x in range(10) for y in range(10)}
print(set_vals)

g = ((x, y) for x in range(10) for y in range(x))
print(type(g))

