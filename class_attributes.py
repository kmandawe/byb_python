import iso6346


class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(owner_code=owner_code, serial=ShippingContainer._get_next_serial())

    @property
    def volume_ft3(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


# c1 = ShippingContainer("YML", "books")
#
# print(c1.owner_code)
# print(c1.contents)
#
# c2 = ShippingContainer("MAE", "clothes")
#
# print(c2.owner_code)
# print(c2.contents)
#
# c4 = ShippingContainer("ESC", "electronics")
# # print(c4.serial)
#
# print(ShippingContainer.next_serial)
# print(c4.next_serial)
# print(c2.next_serial)
#
# c6 = ShippingContainer("YML", "coffee")
# # print(c6.serial)
#
# print(ShippingContainer.next_serial)
#
# c7 = ShippingContainer.create_empty("YML")
# print(c7.contents)

# c8 = ShippingContainer.create_with_items("MAE", ['food', 'textiles', 'minerals'])
# print(c8.contents)
#
# c9 = ShippingContainer.create_empty("YML")
# print(c9.bic)


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6), category='R')

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


# r1 = RefrigeratedShippingContainer("MAE", 'fish')
# print(r1.bic)

bic1 = ShippingContainer._make_bic_code("MAE", 1234)
print(bic1)

bic2 = RefrigeratedShippingContainer._make_bic_code("MAE", 1234)
print(bic2)

# c = ShippingContainer("ESC", "textiles")
# bic1 = c._make_bic_code("MAE", 1234)
# print(bic1)

# r = RefrigeratedShippingContainer("ESC", 'peas')
# bic2 = r._make_bic_code("MAE", 1234)
# print(bic2)

# r2 = RefrigeratedShippingContainer("MAE", "fish")
# print(r2.bic)

# r1 = RefrigeratedShippingContainer.create_empty("YML")
# print(r1)

# r2 = RefrigeratedShippingContainer.create_with_items("YML", ["ice", "peas"])
# print(r2)
# print(r2.contents)

# r3 = RefrigeratedShippingContainer.create_with_items("ESC", ["brocolli", "cauliflower", "carrots"], celsius=2.0)
# print(r3)
# print(r3.bic)
#
# r3.celsius = 12.0


# r4 = RefrigeratedShippingContainer.create_with_items("YML", ["fish"], celsius=-18.0)
# print(r4.celsius)
# r4.celsius = -5.0
#
# r5 = RefrigeratedShippingContainer.create_with_items("YML", ["prawns"], celsius=-18.0)
# print(r5.celsius)
# r5.celsius = -19.0
# print(r5.celsius)
# # r5.celsius = 5.0
#
# r6 = RefrigeratedShippingContainer.create_empty("YML", celsius=-20.0)
# print(r6.fahrenheit)
# r6.fahrenheit = -10.0
# print(r6.celsius)
#
# r7 = RefrigeratedShippingContainer.create_empty("MAE", celsius=7.0)

c = ShippingContainer.create_empty("YML", length_ft=20)
print(c.volume_ft3)

r = RefrigeratedShippingContainer.create_empty("YML", length_ft=20, celsius=-10.0)
print(r.volume_ft3)


class HeatedRefrigeratedShippinContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20.0

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippinContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        super()._set_celsius(value)


h1 = HeatedRefrigeratedShippinContainer.create_empty("YML", length_ft=40, celsius=-18.0)
print(h1)

# h1.celsius = -21.0

# h2 = HeatedRefrigeratedShippinContainer.create_empty("YML", length_ft=40, celsius=-25.0)

# h3 = HeatedRefrigeratedShippinContainer.create_empty("YML", length_ft=40, celsius=5.0)

h4 = HeatedRefrigeratedShippinContainer.create_empty("YML", length_ft=40, celsius=-18.0)
# h4.celsius = 10.0
h4.celsius = -26.0
