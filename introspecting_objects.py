i = 7
print(dir(i))
print(getattr(i, 'denominator'))
print(i.denominator)
print(getattr(i, 'conjugate'))
print(callable(getattr(i, 'conjugate')))
print(i.conjugate.__class__.__name__)
# print(getattr(i, 'index'))
print(hasattr(i, 'bit_length'))
print(hasattr(i, 'index'))

from fractions import Fraction


def mixed_numeral(vulgar):
    if not (hasattr(vulgar, 'numerator') and hasattr(vulgar, 'denominator')):
        raise TypeError("{} is not a rational number".format(vulgar))

    integer = vulgar.numerator // vulgar.denominator
    fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
                        vulgar.denominator)
    return integer, fraction


def mixed_numeral2(vulgar):
    try:
        integer = vulgar.numerator // vulgar.denominator
        fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
                            vulgar.denominator)
        return integer, fraction
    except AttributeError as e:
        raise TypeError("{} is not a rational number".format(vulgar)) from e


print(mixed_numeral(Fraction('11/10')))
# print(mixed_numeral(1.7))


print(mixed_numeral2(1.7))