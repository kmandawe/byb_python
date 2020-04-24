from inheritance_example import SortedIntList, IntList

sil = SortedIntList([42, 23, 2])
print(sil)

# sil = SortedIntList([3, 2, '1'])

sil.add(-1234)
print(sil)
# sil.add('the smallest uninteresting number')


class Base1:
    def __init__(self):
        print('Base1.__init__')


class Base2:
    def __init__(self):
        print('Base2.__init__')


class Sub(Base1, Base2):
    pass


s = Sub()

print(SortedIntList.__bases__)

print(IntList.__bases__)