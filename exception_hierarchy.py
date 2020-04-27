s = [1, 4, 6]

# print(s[5])

d = dict(a=65, b=66, c=67)

# print(d['x'])

print(IndexError.mro())

print(KeyError.mro())


def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except LookupError:
        print("Handled IndexError")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except LookupError:
        print("Handled KeyError")


if __name__ == '__main__':
    lookups()