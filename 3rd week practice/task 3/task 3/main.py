import turtle

import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('orders.csv', header=None,
                 names=['code', 'product_name', 'month_number', 'base_price', 'quantity', 'total_price'])

# Get the customer code from the user
customer_code = input("Enter the customer code: ")

# Filter the DataFrame based on the customer code
filtered_df = df[df['code'] == customer_code]

# Check if no rows with the entered customer code exist, and print an error message if so
if filtered_df.empty:
    print("Incorrect customer code. The specified customer was not found.")
else:
    # Create three series for the charts
    sales_quantity_series = filtered_df.groupby('month_number')['quantity'].sum()
    price_series = filtered_df.groupby('month_number')['base_price'].sum()
    product_quantity_series = filtered_df.groupby('product_name')['quantity'].sum()

    # Plot the sales quantity per month chart
    plt.figure(figsize=(6, 4))
    sales_quantity_series.plot(marker='o', title='Sales Quantity per Month')
    plt.xlabel('Month')
    plt.ylabel('Sales Quantity')

    # Save the sales quantity per month chart as an image
    plt.savefig('sales_quantity_chart.png')
    plt.close()

    # Plot the price per month chart
    plt.figure(figsize=(6, 4))
    price_series.plot(marker='o', title='Price per Month')
    plt.xlabel('Month')
    plt.ylabel('Price')

    # Save the price per month chart as an image
    plt.savefig('price_chart.png')
    plt.close()

    # Print the product quantity for the specified customer
    print("Product Quantity for Customer", customer_code)
    print(product_quantity_series)

    # Use turtle to display the charts
    turtle.screensize(800, 600)
    turtle.title("Sales Analysis")
    turtle.bgcolor("white")

    # Display the sales quantity per month chart
    sales_quantity_chart = turtle.Turtle()
    sales_quantity_chart.penup()
    sales_quantity_chart.goto(-350, 250)
    sales_quantity_chart.pendown()
    sales_quantity_chart.color('blue')
    for month, quantity in sales_quantity_series.items():
        sales_quantity_chart.goto(month * 50, quantity * 10)
    sales_quantity_chart.hideturtle()

    # Display the price per month chart
    price_chart = turtle.Turtle()
    price_chart.penup()
    price_chart.goto(-350, -250)
    price_chart.pendown()
    price_chart.color('red')
    for month, price in price_series.items():
        price_chart.goto(month * 50, price)
    price_chart.hideturtle()

    turtle.done()
