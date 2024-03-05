import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('orders.csv', header=None,
                 names=['code', 'product_name', 'month_number', 'base_price', 'quantity', 'total_price'])

# Get the product name from the user
product_name = input("Enter the product name: ")

# Filter the DataFrame based on the product name
filtered_df = df[df['product_name'] == product_name]

# Check if no rows with the entered product name exist, and print an error message if so
if filtered_df.empty:
    print("Incorrect product name. The specified product was not found.")
else:
    # Create two series for the charts
    sales_series = filtered_df.groupby('month_number')['quantity'].sum()
    price_series = filtered_df.groupby('month_number')['base_price'].mean()

    # Plot the charts
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    sales_series.plot(ax=axes[0], marker='o', title='Sales Quantity per Month')
    axes[0].set_xlabel('Month')
    axes[0].set_ylabel('Sales Quantity')

    price_series.plot(ax=axes[1], marker='o', title='Price Changes per Month')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Price')

    plt.tight_layout()
    plt.show()
