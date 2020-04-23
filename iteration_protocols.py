class ExampleIterator:
    def __init__(self):
        self.index = 0
        self.data = [1, 2, 3]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        rslt = self.data[self.index]
        self.index += 1
        return rslt


i = ExampleIterator()
print(next(i))
print(next(i))
print(next(i))
# print(next(i))


i = ExampleIterator()
for i in ExampleIterator():
    print(i)
