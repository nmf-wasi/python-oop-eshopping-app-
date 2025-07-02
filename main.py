from eShopping import E_Shopping
from seller import Seller
from customer import Customer

eshopping = E_Shopping("Panda Mart")

def seller_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    seller = Seller(name, email)
    eshopping.add_sellers(seller)

    while True:
        print(f"Welcome {seller.name}")
        print("1. Add new product")
        print("2. Exit Seller Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            seller.addProduct()
        elif choice == 2:
            break
        else:
            print("Invalid Choice")


def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    customer = Customer(name, email)
    eshopping.add_customer(customer)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View All Products")
        print("2. Place Order")
        print("3. Exit Customer Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer.see_all_products()
        elif choice == 2:
            customer.place_order()
        elif choice == 3:
            break
        else:
            print("Invalid Choice")


while(True):
    print("Welcome")
    print("1. Customer")
    print("2. Seller")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        customer_menu()
    elif choice==2:
        seller_menu()
    elif choice==3:
        break
    else:
        print("Invalid Input")