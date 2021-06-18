import iso6346

class ShippingContainer:

    next_serial = 1111

    @staticmethod
    def _make_code_bic(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def _generate_serial(cls):
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result


    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)


    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_code_bic(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


container = ShippingContainer("FRU", ["bananas", "apples", "peaches"])
print(1, container.owner_code, container.contents, container.bic)

container_1 = ShippingContainer("ELC", ["computers", "battery", "cables"])
print(2, container_1.owner_code, container_1.contents, container_1.bic)

container_2 = ShippingContainer.create_with_items("MIN", ["coal", "iron", "silver"])
print(3, container_2.owner_code, container_2.contents, container_2.bic)

container_3 = ShippingContainer.create_empty("CLO")
print(4, container_3.owner_code, container_3.contents, container_3.bic)
