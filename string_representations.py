class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, format_spec):
        if format_spec == 'r':
            return "{}, {}".format(self.y, self.x)
        else:
            return "{}, {}".format(self.x, self.y)


# p = Point2D(x=42, y=69)
# print(p)
# print(str(p))
# print(repr(p))
#
# p = Point2D(123, 456)
# print(str(p))
# print("The circle is centered at {}.".format(p))
# print("The circle is centered at {}.".format(repr(p)))
#
# print(Point2D(3, 5))

# l = [Point2D(i, i * 2) for i in range(3)]
# print(str(l))
# print(repr(l))
#
# d = {i: Point2D(i, i * 2) for i in range(3)}
# print(str(d))
# print(repr(d))


# print("This is a point: {}".format(Point2D(1, 2)))
#
# print("{}".format(Point2D(1, 2)))
# print("{:r}".format(Point2D(1, 2)))
# print("{!r}".format(Point2D(1, 2)))
# print("{!s}".format(Point2D(1, 2)))
#
# import reprlib
# points = [Point2D(x, y) for x in range(1000) for y in range(1000)]
# print(len(points))
# print(reprlib.repr(points))

x = "HÁLLO"
print(x)
print(type(x))
y = ascii(x)
print(y)
print(type(y))

x = '¾'
print(ord(x))
print(chr(190))
print(chr(ord()))
print(ord(chr(190)))


