import csv
import json
import random
import numpy as np


class Order:
    def __init__(self, customer_code, product_name, month_number, base_price, quantity):
        self.customer_code = customer_code
        self.product_name = product_name
        self.month_number = month_number
        self.base_price = base_price
        self.quantity = quantity
        self.final_amount = base_price * quantity

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
            'month_number': int(self.month_number),  # Convert to Python integer
            'base_price': float(self.base_price),  # Convert to Python float
            'quantity': int(self.quantity),
            'final_amount': float(self.final_amount)  # Convert to Python float
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

# Generate random values for each attribute using NumPy arrays
customer_codes = np.array(["C" + str(random.randint(1, 1000)).zfill(3) for _ in range(num_orders)])
product_names = np.array(["Product " + str(random.randint(1, 10)) for _ in range(num_orders)])
month_numbers = np.random.randint(1, 12, size=num_orders)
base_prices = np.random.uniform(10, 100, size=num_orders)
quantities = np.random.randint(1, 5, size=num_orders)

# Calculate final amounts using vectorized operations
final_amounts = base_prices * quantities

# Create an array of Order instances
orders = np.array([Order(customer_codes[i], product_names[i], month_numbers[i], base_prices[i], quantities[i]) for i in
                   range(num_orders)])

# Display order details and save to files
for order in orders:
    order.display_order_details()
    order.save_to_csv('orders.csv')
    order.save_to_json('orders.json')
