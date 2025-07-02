class Product:
    products = {}

    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    @classmethod
    def add_product(self):
        product_name = input("Enter Product Name: ").lower()
        product_stock = int(input("Enter Product Quantity: "))
        if product_name in self.products:
            self.products[product_name] += product_stock
        else:
            self.products[product_name] = product_stock
    @classmethod
    def see_all_products(self):
        if not self.products:
            print("No products available!")
        else:
            for name, stock in self.products.items():
                if int(stock) > 0:
                    print(f"{name}: stock: {stock}")
        print()
    @classmethod
    def place_order(self):
        name = input("Enter the name of the product: ").lower()
        if name not in self.products:
            print(f"Sorry {name} isn't available")
            return
        
        order_quantity = int(input(f"Enter the amount of {name} you want to order: "))
        available_quantity = int(self.products[name])
        if order_quantity > available_quantity:
            print(f"Sorry, that amount of {name} isn't avaible right now")
        else:
            self.products[name] -= order_quantity
            print("Order placed successfully!")
