class ShippingContainer:

    next_serial = 7899

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

container = ShippingContainer("Joan Due", ["bananas", "apples", "peaches"])
print(container.owner_code)
print(container.contents)
print(container.next_serial)

container_1 = ShippingContainer("Sue Try", ["computers", "battery", "cables"])
print(container_1.owner_code)
print(container_1.contents)
print(container_1.serial)

container_2 = ShippingContainer("Max Bold", ["coal", "iron", "silver"])
print(container_2.owner_code)
print(container_2.contents)
print(container_2.serial)