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
    def create_empty(cls, owner_code):
        return cls(owner_code, None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._make_bic_code(owner_code=owner_code, serial=ShippingContainer._get_next_serial())


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

