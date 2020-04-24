from inheritance_example import SortedIntList

print(SortedIntList.__mro__)
print(SortedIntList.mro())


class A:
    def func(self):
        return 'A.func'


class B(A):
    def func(self):
        return 'B.func'


class C(A):
    def func(self):
        return 'C.func'


class D(C, B):
    pass


print(D.mro())

d = D()
print(d.func())

print(SortedIntList.mro())