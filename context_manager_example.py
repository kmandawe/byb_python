with open('important_data.txt', 'w') as f:
    f.write('The secret password is 12345')


class LoggingContextManager:

    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'You are in a with-block!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__:'
                  'normal exit detected.')
        else:
            print('LoggingContextManager.__exit__:'
                  'Exception detected!'
                  'type={}, value={}, traceback={}'.format(exc_type, exc_val, exc_tb))


with LoggingContextManager() as x:
    # raise ValueError('Something has gone wrong!')
    print(x)


f = open('a_file', 'w')
with f as g:
    print(f is g)


with LoggingContextManager():
    pass

# with LoggingContextManager():
#     raise ValueError("Core meltdown imminent!")

try:
    with LoggingContextManager():
        raise ValueError("The system is down!")
except ValueError:
    print("*** ValueError detected ***")
