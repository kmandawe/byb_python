l = [i * 2 for i in range(10)]
print(l)
print(dir(l))
print(l.append(42))
print(l)
d = {i: i * 2 for i in range(10)}
print(type(d))
s = {i for i in range(10)}
print(type(s))
g = (i for i in range(10))
print(type(g))

c = [(x, y) for x in range(5) for y in range(3)]
print(c)

points = []
for x in range(5):
    for y in range(3):
        points.append((x, y))

print(points)

values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0]
print(values)

new_values = [(x, y) for x in range(10) for y in range(x)]
print(new_values)

