from person import Person
from product import Product


class Seller(Person):
    def __init__(self, name, email):
        super().__init__(name, email)

    def addProduct(self):
        Product.add_product()
