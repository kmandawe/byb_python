def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print("Calling {}".format(f))
            return f(*args, **kwargs)

        return wrap


tracer = Trace()


@tracer
@escape_unicode
def norweigian_island_maker(name):
    return name + "ðy"


print(norweigian_island_maker("Llama"))
print(norweigian_island_maker("Python"))
print(norweigian_island_maker("Troll"))

tracer.enabled = False

print(norweigian_island_maker("Llama"))
print(norweigian_island_maker("Python"))
print(norweigian_island_maker("Troll"))


tracer.enabled = True


class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix


im = IslandMaker(" Island")
print(im.make_island("Python"))
print(im.make_island("Llama"))


