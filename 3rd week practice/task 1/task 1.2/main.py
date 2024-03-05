import csv
import json
import random


class Order:
    def __init__(self, _customer_code, _product_name, _month_number, _base_price, _quantity):
        self.customer_code = _customer_code
        self.product_name = _product_name
        self.month_number = _month_number
        self.base_price = _base_price
        self.quantity = _quantity
        self.final_amount = _base_price * _quantity

    def display_order_details(self):
        print("Customer Code:", self.customer_code)
        print("Product Name:", self.product_name)
        print("Month Number:", self.month_number)
        print("Base Price:", self.base_price)
        print("Quantity:", self.quantity)
        print("Final Amount:", self.final_amount)
        print("---------------------------")

    def save_to_csv(self, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.customer_code, self.product_name, self.month_number, self.base_price, self.quantity,
                             self.final_amount])

    def save_to_json(self, filename):
        order_data = {
            'customer_code': self.customer_code,
            'product_name': self.product_name,
            'month_number': self.month_number,
            'base_price': self.base_price,
            'quantity': self.quantity,
            'final_amount': self.final_amount
        }
        with open(filename, 'a') as file:
            json.dump(order_data, file)
            file.write('\n')


# Get the number of orders from the user
try:
    num_orders = int(input("Enter the number of orders to generate: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Create a list of random orders
orders = ''
orders = list(orders)
for _ in range(num_orders):
    customer_code = "C" + str(random.randint(1, 1000)).zfill(3)
    product_name = "Product " + str(random.randint(1, 10))
    month_number = random.randint(1, 12)
    base_price = random.uniform(10, 100)
    quantity = random.randint(1, 5)
    order = Order(customer_code, product_name, month_number, base_price, quantity)
    orders.append(order)

# Display order details and save to files
for order in orders:
    order.display_order_details()
    order.save_to_csv('orders.csv')
    order.save_to_json('orders.json')
