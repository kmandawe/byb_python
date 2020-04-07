class CallCount:
    def __init__(self, f):
        print("Calling init....")
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        print("Calling call....")
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print("Hello, {}".format(name))


hello("Fred")
hello("Wilma")
hello("Betty")
hello("Barney")

print(hello.count)
