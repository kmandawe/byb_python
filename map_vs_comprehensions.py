for_list = [str(i) for i in range(5)]
print(for_list)

map_list = list(map(str, range(5)))
print(map_list)

i = (str(i) for i in range(5))
print(list(i))

i = map(str, range(5))
print(list(i))

