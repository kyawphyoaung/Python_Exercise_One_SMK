# POS Software
# Product
# Add to Cart
# Check out
# View Orders
# Customer 

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
p_one = Product("Laptop","800USD",10)


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self,product_id,name,price,quantity):
        self.products[product_id] = Product(name,price,quantity)

    def display_inventory(self):
        print("\nDisplay Product")
        for product_id, product in self.products.items():
            print(f"ID: {product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")  

    def process_sale(self,product_id,quantity):
        user_request_product = self.products[product_id]
        total_price = user_request_product.price * quantity
        return total_price

# products[2] <= Product("Keyboard",40,12)
# Product(name,price,quantity)
# products[2].price

# for item in items:
#        print(item)

inventory_obj = Inventory()
inventory_obj.add_product(1,"Laptop",800,10)
inventory_obj.add_product(2,"Keyboard",40,12)
inventory_obj.add_product(3,"Speaker",80,22)
inventory_obj.add_product(4,"Camera",240,39)


class Customer:
    def __init__(self,name = None):
        self.name = name

customer = Customer()

def check_customer_name(customer):
    if customer.name is None:
        print("You haven't entered the customer name.")
        customer_name = input("Enter customer name: ")
        customer.name = customer_name
    return customer.name

def display_menu():
    print("\nMenu:")
    print("1. Display Product")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Check out")
    print("5. View Orders")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        inventory_obj.display_inventory()
    elif choice == '2':
        print("Add to cart")
        customer_name = check_customer_name(customer)
        product_id = int(input("Enter the product ID: "))
        quantity = int(input("Enter the quantity: "))
        total_price = inventory_obj.process_sale(product_id,quantity)
        print(f"Total Price : {total_price}")
    elif choice == '3':
        print("View cart")
    elif choice == '4':
        print("Check out")
    elif choice == '5':
        print("View Orders")
    elif choice == '6':
        print("Program exit. Thank you!")
        break
    else:
        print("Invalid code.Please enter nubmer between 1-6")

