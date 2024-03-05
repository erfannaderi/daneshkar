import tkinter as tk

import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('orders.csv', header=None)

# Extract the product name column
product_name = df.iloc[:, 1]

# Calculate the total sales for each product
product_sales = product_name.value_counts().head(5)

# Calculate the total orders and sales for each month
monthly_orders = df.iloc[:, 4].value_counts()
monthly_sales = df.iloc[:, 5].groupby(df.iloc[:, 4]).sum()

# Create a GUI window
window = tk.Tk()
window.title("Sales Report")


# Function to display the top 5 products sales
def show_product_sales():
    product_sales.plot(kind='bar', rot=0)
    plt.title('Top 5 Best Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.show()


# Function to display the monthly orders
def show_monthly_orders():
    monthly_orders.plot(kind='bar', rot=0)
    plt.title('Monthly Orders')
    plt.xlabel('Month')
    plt.ylabel('Number of Orders')
    plt.show()


# Function to display the monthly sales
def show_monthly_sales():
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales Quantity')
    plt.show()


# Create buttons to trigger the plots
product_sales_button = tk.Button(window, text="Top 5 Products Sales", command=show_product_sales)
product_sales_button.pack(pady=10)

monthly_orders_button = tk.Button(window, text="Monthly Orders", command=show_monthly_orders)
monthly_orders_button.pack(pady=10)

monthly_sales_button = tk.Button(window, text="Monthly Sales", command=show_monthly_sales)
monthly_sales_button.pack(pady=10)

# Run the GUI main loop
window.mainloop()
