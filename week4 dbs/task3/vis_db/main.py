import sys
import matplotlib.pyplot as plt
import pandas as pd
import json
import redis

# Connect to the Redis database
r = redis.Redis(host='chogolisa.liara.cloud', port=30865, password='HVot0dzPdZTVYKKnevYYvJuc')

# Retrieve data from Redis and load it into a pandas DataFrame
data = [json.loads(r.get(key)) for key in r.keys()]
df = pd.DataFrame(data)

# Extract the product name column
product_name = df['product_name']

# Calculate the total sales for each product
product_sales = product_name.value_counts().head(5)

# Calculate the total orders and sales for each month
monthly_orders = df['month_number'].value_counts()
monthly_sales = df.groupby('month_number')['final_amount'].sum()

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
