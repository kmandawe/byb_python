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
def rotate_list(l):
    return l[1:] + [l[0]]


my_list = [1, 2, 3]
my_list = rotate_list(my_list)
print(my_list)
my_list = rotate_list(my_list)
print(my_list)
my_list = rotate_list(my_list)
print(my_list)

print("Disabling tracer")
tracer.enabled = False
my_list = rotate_list(my_list)
print(my_list)




