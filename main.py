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
    
    def display_selected(self,selected_product):
        for product_id, product in self.products.items():
            if(selected_product==product_id):
                return product.name
        return False

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

class Order():
    def __init__(self):
        self.products = {}
        self.total = 0

class Cart:
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_item(self,product_id,quantity,price):
        self.items[product_id] = {'quantity' : quantity , 'price': price}
        self.total += price

    def display_cart(self):
        customer_name = check_customer_name(customer)
        print(f"\n Customer: {customer_name}")
        print("Shopping Cart")
        for product_id, item in self.items.items():
            product_name = inventory_obj.display_selected(product_id)
            print(f"ID: {product_id}, Product name: {product_name}, Quantity: {item['quantity']}, Price: {item['price']}")
        print(f"Total Price: ${self.total}")

    def checkout(self):
        order = Order()
        order.products = self.items
        order.total = self.total
        self.items = {}
        self.total = 0
        print("Check out compeleted!")
        return order


class Customer:
    def __init__(self,name = None):
        self.name = name
        self.cart = Cart()
        self.orders = []

    def view_orders(self):
        for i,order in enumerate(self.orders, 1):
            print(f"Order {i}")
            for product_id,product in order.products.items():
                print(f"ID: {product_id}, Name: {inventory_obj.display_selected(product_id)}, Quantity: {product['quantity']}, Price: {product['price']}")
            print(f"Total Amount: {order.total}")

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
        product_name = inventory_obj.display_selected(product_id)
        if(product_name):
            print(f"Product Name: {product_name}")
            quantity = int(input("Enter the quantity: "))
            total_price = inventory_obj.process_sale(product_id,quantity)
            print(f"Total Price : {total_price}")
            customer.cart.add_item(product_id,quantity,total_price)
            print("Product added to the cart")
        else:
            print("This product is not available")
    elif choice == '3':
        print("View cart")
        customer.cart.display_cart()
    elif choice == '4':
        print("Check out")
        order = customer.cart.checkout()
        customer.orders.append(order)
    elif choice == '5':
        print("View Orders")
        customer.view_orders()
    elif choice == '6':
        print("Program exit. Thank you!")
        break
    else:
        print("Invalid code.Please enter nubmer between 1-6")

