from person import Person
from product import Product


class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name, email)

    def see_all_products(self):
        Product.see_all_products()
    def place_order(self):
        Product.place_order()