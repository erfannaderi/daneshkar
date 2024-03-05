import sys

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

# Check if the "-r" or "--report" argument is passed
if len(sys.argv) > 1 and (sys.argv[1] == '-r' or sys.argv[1] == '--report'):
    # Plot the top 5 products sales
    product_sales.plot(kind='bar', rot=0)
    plt.title('Top 5 Best Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.show()

    # Plot the monthly orders
    monthly_orders.plot(kind='bar', rot=0)
    plt.title('Monthly Orders')
    plt.xlabel('Month')
    plt.ylabel('Number of Orders')
    plt.show()

    # Plot the monthly sales
    monthly_sales.plot(kind='line', marker='o')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales Quantity')
    plt.show()
else:
    print("No report argument passed.")
