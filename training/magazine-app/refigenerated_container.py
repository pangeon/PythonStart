import iso6346
from shipping_container import ShippingContainer

class RefigeneratedContainer(ShippingContainer):

    MAX_CELSIUS = 3.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > RefigeneratedContainer.MAX_CELSIUS:
            raise ValueError("Temperature is too high")

    @staticmethod
    def _make_code_bic(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )


container_4 = RefigeneratedContainer("PHU", ["books", "shylesheet", "scissors"], celsius=2)
print(5, container_4.owner_code, container_4.contents, container_4.bic)

container_5 = RefigeneratedContainer.create_with_items("ESC", ["bean", "tomatoes", "carrots"], celsius=3)
container_5.celsius = 100
print(6, container_5.owner_code, container_5.contents, container_5.bic, container_5.celsius)