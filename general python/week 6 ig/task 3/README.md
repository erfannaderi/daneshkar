# Save Numbers Smaller than a Given Number to CSV

This Python script allows you to input a number and generates numbers smaller than that number, saving them to a CSV file using a decorator and a generator.

## How to Use

1. Install Python on your system.
2. Copy and paste the provided code into a Python script file (e.g., save_numbers_to_csv.py).
3. Run the script in a Python environment.
4. Enter a number when prompted.
5. The script will generate numbers smaller than the input number and save them to a CSV file named numbers.csv.

## Code Overview

- The save_to_csv decorator is used to save the result of a function to a CSV file.
- The generate_numbers function generates numbers smaller than a given number using a generator expression.
- The script takes user input for a number, generates smaller numbers, and saves them to a CSV file.

## Usage

1. Define the save_to_csv decorator.
2. Decorate the desired function (e.g., generate_numbers) with @save_to_csv.
3. Run the script and enter a number when prompted.
4. Check the numbers.csv file for the generated numbers.
