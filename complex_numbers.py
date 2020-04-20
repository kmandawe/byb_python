print(2j)
print(3 + 4j)
print(type(3 + 4j))
print(complex(3))
print(complex(-2, 3))
print(complex('(-2+3j)'))
print(complex('-2+3j'))
# print(complex('-2 + 3j'))


c = 3 + 5j
print(c.real)
print(c.imag)
print(c.conjugate())

import math
# math.sqrt(-1)

import cmath

print(cmath.sqrt(-1))

print(cmath.phase(1 + 1j))

print(abs(1 + 1j))

print(cmath.polar(1 + 1j))

modulus, phase = cmath.polar(1 + 1j)
print(modulus)
print(phase)

print(cmath.rect(modulus, phase))


def inductive(ohms):
    return complex(0.0, ohms)


def capacitive(ohms):
    return complex(0.0, -ohms)


def resistive(ohms):
    return complex(ohms)


def impedance(components):
    z = sum(components)
    return z

i = impedance([inductive(10), resistive(10), capacitive(5)])
print(i)
print(cmath.phase(i))
print(math.degrees(cmath.phase(i)))