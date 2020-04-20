from decimal import Decimal
from fractions import Fraction

two_thirds = Fraction(2, 3)
print(two_thirds)

four_fifths = Fraction(4, 5)
print(four_fifths)

# print(Fraction(5, 0))

print(Fraction(92343475452352346823412352346))
print(Fraction(0.5))
print(Fraction(0.1))
print(Fraction(Decimal('0.1')))
print(Fraction('22/7'))

print(Fraction(2, 3) + Fraction(4, 5))
print(Fraction(2, 3) - Fraction(4, 5))
print(Fraction(2, 3) * Fraction(4, 5))
print(Fraction(2, 3) / Fraction(4, 5))
print(Fraction(2, 3) // Fraction(4, 5))
print(Fraction(2, 3) % Fraction(4, 5))

from math import floor
print(floor(Fraction('4/3')))

