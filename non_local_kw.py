import time

message = "global"


def enclosing():
    message = "enclosing"

    def local():
        # global message
        nonlocal message
        message = "local"

    print("enclosing message:", message)
    local()
    print("enclosing message:", message)


print("global message", message)
enclosing()
print("global message", message)


def make_timer():
    last_called = None

    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return elapsed


t = make_timer()
print(t())
print(t())
print(t())

t1 = make_timer()
t2 = make_timer()

print(t1())
print(t1())
print(t2())
print(t2())
print(t1())
print(t2())
