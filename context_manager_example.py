with open('important_data.txt', 'w') as f:
    f.write('The secret password is 12345')


class LoggingContextManager:

    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'You are in a with-block!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('LoggingContextManager.__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
        return


with LoggingContextManager() as x:
    raise ValueError('Something has gone wrong!')
    print(x)

