sizes = ["small", "medium", "large"]
colors = ["lavender", "tea", "burnt orange"]
animals = ["koala", "platypus", "salamander"]


def combine(size, color, animal):
    return "{} {} {}".format(size, color, animal)


combined = list(map(combine, sizes, colors, animals))
print(combined)

import itertools


def combine(quantity, size, color, animal):
    return "{} x {} {} {}".format(quantity, size, color, animal)


combined = list(map(combine, itertools.count(), sizes, colors, animals))
print(combined)
