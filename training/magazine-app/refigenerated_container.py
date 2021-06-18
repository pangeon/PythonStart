import iso6346
from shipping_container import ShippingContainer

class RefigeneratedContainer(ShippingContainer):
    @staticmethod
    def _make_code_bic(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"
        )


container_4 = RefigeneratedContainer("PHU", ["books", "shylesheet", "scissors"])
print(5, container_4.owner_code, container_4.contents, container_4.bic)