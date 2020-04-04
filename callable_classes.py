def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls


seq = sequence_class(immutable=True)

t = seq("Timbuktu")
print(t)
print(type(t))