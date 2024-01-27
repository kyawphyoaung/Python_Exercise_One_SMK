# POS Software
# Product
# Add to Cart
# Check out
# View Orders
# Customer 
import csv
import tkinter as tk
from tkinter import messagebox,simpledialog
from tkinter import ttk

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
        with open('add_to_cart.csv',mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            cart_data = [ row for row in reader ]
        
        return cart_data

    def checkout(self,customer_name):
        order = Order()
        order.products = self.items
        order.total = self.total
        self.items = {}
        self.total = 0
        with open('add_to_cart.csv',mode='r') as file:
            reader = csv.reader(file)
            cart_data = [row for row in reader]

        cus_name_check_cart = [row for row in cart_data if row[0] == customer_name]

        if(cus_name_check_cart):
            cart_data = [row for row in cart_data if row[0]!= customer_name]

            with open('add_to_cart.csv','w',newline='') as file:
                writer = csv.writer(file)
                writer.writerows(cart_data)
            
            print("Check out compeleted!")
            messagebox.showinfo("Checkout Status","Checkout Successfull!")

            total_amount = 0

            with open('orders.csv',mode='r') as file:
                reader = csv.reader(file)
                header = next(reader)
                order_data = [row for row in reader]

            for row in order_data:
                order_id = int(row[0])
                
            for row in cus_name_check_cart:
                total_amount += int(row[5])

            for row in cus_name_check_cart:
                row.insert(0,order_id+1)
                row.append(total_amount)

            with open('orders.csv',mode='a',newline='\n') as file:
                writer = csv.writer(file)
                writer.writerows(cus_name_check_cart)

            return order
        else:
            messagebox.showinfo("Checkout Status","Invalid Customer Name!")

        


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
        customer_name = simpledialog.askstring("Customer Name","Enter customer name")
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

# while True:
#     display_menu()
#     choice = input("Enter your choice: ")

#     if choice == '1':
#         inventory_obj.display_inventory()
#     elif choice == '2':
#         print("Add to cart")
#         customer_name = check_customer_name(customer)
#         product_id = int(input("Enter the product ID: "))
#         product_name = inventory_obj.display_selected(product_id)
#         if(product_name):
#             print(f"Product Name: {product_name}")
#             quantity = int(input("Enter the quantity: "))
#             total_price = inventory_obj.process_sale(product_id,quantity)
#             print(f"Total Price : {total_price}")
#             customer.cart.add_item(product_id,quantity,total_price)
#             print("Product added to the cart")
#         else:
#             print("This product is not available")
#     elif choice == '3':
#         print("View cart")
#         customer.cart.display_cart()
#     elif choice == '4':
#         print("Check out")
#         order = customer.cart.checkout()
#         customer.orders.append(order)
#     elif choice == '5':
#         print("View Orders")
#         customer.view_orders()
#     elif choice == '6':
#         print("Program exit. Thank you!")
#         break
#     else:
#         print("Invalid code.Please enter nubmer between 1-6")

class POSApp:
    def __init__(self,root):
        self.root = root
        self.root.title("POS Sytem")
        self.create_main_frame()
        self.create_buttons()

    def create_main_frame(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack()

        self.tree = ttk.Treeview(main_frame,columns=("ID","Name","Price","Quantity"),show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")

        self.tree.column("ID", width=50)
        self.tree.column("Name", width=100)
        self.tree.column("Price", width=100)
        self.tree.column("Quantity", width=100)

        for product_id, product in inventory_obj.products.items():
            print(f"ID: {product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
            self.tree.insert("","end",values=(product_id,product.name,product.price,product.quantity))

        self.tree.pack(pady=10)
    
    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        buttons = [
            ("Add to cart", self.add_to_cart),
            ("Display cart",self.display_cart_btn),
            ("Check out", self.checkout_btn),
            ("View Order", self.view_orders )
        ]

        for texts, commands in buttons:
            tk.Button(button_frame,text=texts, command=commands).pack(side=tk.LEFT, padx=5)

    def display_cart_btn(self):
        cart_items = customer.cart.display_cart()
        view_cart_window = TableWindow(self.root,"Display Cart",["Customer Name","Product ID","Product Name","Quantity","Price","Total"],cart_items)
        view_cart_window.title("View Cart")

    def add_to_cart(self):
        customer_name = check_customer_name(customer)
        product_id = simpledialog.askinteger("Input","Enter the product ID")
        product_name = inventory_obj.display_selected(product_id)
        if(product_name):
            quantity = simpledialog.askinteger(f"{product_name}","Enter the quantity")
            total_price = inventory_obj.process_sale(product_id,quantity)
            result = "Customer : " + f"{customer_name}"
            result += "\nTotal Price: " + f"{total_price}"
            # result = Total Price : 100
            customer.cart.add_item(product_id,quantity,total_price)
            with open('add_to_cart.csv',mode='a',newline="\n") as file:
                writer = csv.writer(file)
                writer.writerow([customer_name,product_id,product_name,quantity,int(total_price/quantity),total_price])

            result += "\nProduct added to the cart"
        else:
            result = "This product is not available"
        messagebox.showinfo("Add to cart",result)

    def checkout_btn(self):
        customer_name = simpledialog.askstring("Customer Name","Enter customer name")
        order = customer.cart.checkout(customer_name)
        customer.orders.append(order)

    def view_orders(self):
        with open('orders.csv',mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            order_data = [ row for row in reader ]

        order_window = TableWindow(self.root,"Display Order",["Order_No","Customer Name","ID","Product Name","Quantity","Unit Price","Total Price","Total Amount"],order_data)
        order_window.title("Display Order")

class TableWindow(tk.Toplevel):
    def __init__(self,parent,title,columns,data):
        super().__init__(parent)
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
        
        for row in data:
            self.tree.insert("","end",values=row)

        self.tree.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()
