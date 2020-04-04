print()
print("one")
print("one", "two")
print("one", "two", "three")
print("{a}<====>{b}".format(a="Oslo", b="Stavanger"))


def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


print(hypervolume(2, 4))
print(hypervolume(2, 4, 6))
print(hypervolume(2, 4, 6, 8))
print(hypervolume(1))


# print(hypervolume())


def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result


result_tag = tag('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1)
print(result_tag)


# not allowed
# def print_args(**kwargs, *args):

def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


print_args(1, 2, 3, 4, 5)


def print_args(arg1, arg2, *args, kwarg1, kwarg2):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)


print_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7)


# will throw TypeError
# print_args(1, 2, 3, 4, 5, 6, 7)

def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


print_args(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7, kwarg3=8, kwarg4=9)

# not allowed
# def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs, kwargs99):
