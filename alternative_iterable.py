class AlternativeIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, item):
        return self.data[item]


print([i for i in AlternativeIterable()])

