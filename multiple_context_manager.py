import contextlib


@contextlib.contextmanager
def nest_test(name):
    print("Entering", name)
    yield name
    print("Exiting", name)


with nest_test('outer'), nest_test('inner'):
    print('BODY')


with nest_test('outer'):
    with nest_test('inner'):
        print("BODY")


with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
    print("BODY")


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise


with propagater('outer', True), propagater('inner', False):
    raise TypeError("Cannot convert load into gold.")


with propagater('outer', False), propagater('inner', True):
    raise TypeError("Cannot convert load into gold.")


