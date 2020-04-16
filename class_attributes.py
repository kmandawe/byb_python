import iso6346


class ShippingContainer:
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
    def create_empty(cls, owner_code, *args, **kwargs):
        return cls(owner_code, None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(owner_code=owner_code, serial=ShippingContainer._get_next_serial())


c1 = ShippingContainer("YML", "books")

print(c1.owner_code)
print(c1.contents)

c2 = ShippingContainer("MAE", "clothes")

print(c2.owner_code)
print(c2.contents)

c4 = ShippingContainer("ESC", "electronics")
# print(c4.serial)

print(ShippingContainer.next_serial)
print(c4.next_serial)
print(c2.next_serial)

c6 = ShippingContainer("YML", "coffee")
# print(c6.serial)

print(ShippingContainer.next_serial)

c7 = ShippingContainer.create_empty("YML")
print(c7.contents)

c8 = ShippingContainer.create_with_items("MAE", ['food', 'textiles', 'minerals'])
print(c8.contents)

c9 = ShippingContainer.create_empty("YML")
print(c9.bic)


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6), category='R')

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self.celsius = celsius


# r1 = RefrigeratedShippingContainer("MAE", 'fish')
# print(r1.bic)

bic1 = ShippingContainer._make_bic_code("MAE", 1234)
print(bic1)

bic2 = RefrigeratedShippingContainer._make_bic_code("MAE", 1234)
print(bic2)

c = ShippingContainer("ESC", "textiles")
bic1 = c._make_bic_code("MAE", 1234)
print(bic1)

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

r3 = RefrigeratedShippingContainer.create_with_items("ESC", ["brocolli", "cauliflower", "carrots"], celsius=2.0)
print(r3)
print(r3.bic)

r3.celsius = 12.0

