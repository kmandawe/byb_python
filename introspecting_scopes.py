print(globals())
a = 42
print(globals())
globals()['tau'] = 6.283185
print(tau)
print(tau / 2)
print(locals())


def report_scope(arg):
    from pprint import pprint as pp
    x = 496
    pp(locals(), width=10)


report_scope(42)

name = "Joe Bloggs"
age = 28
country = "New Zealand"
print("{name} is {age} years old and is from {country}".format(**locals()))