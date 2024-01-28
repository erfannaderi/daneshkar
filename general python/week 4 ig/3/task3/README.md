# README.md

This README.md file provides an overview of the Python code that calculates the factorial of a number using different approaches. The code includes five different functions, each implementing a different approach to calculate the factorial. 

## Functions

### `factorial_math(number_input: int) -> int`

This function calculates the factorial of a given number using the `math.factorial` function from the `math` module. The function takes an integer `number_input` as input and returns the factorial of that number as an integer.

### `factorial_recursive(number_input: int) -> int`

This function calculates the factorial of a given number using a recursive approach. It uses a base case where if the `number_input` is 0, it returns 1. Otherwise, it recursively calls itself with `number_input - 1` and multiplies it with `number_input`. The function takes an integer `number_input` as input and returns the factorial of that number as an integer.

### `factorial_reduce(number_input: int) -> int`

This function calculates the factorial of a given number using the `reduce` function from the `functools` module and the `mul` function from the `operator` module. It uses the `reduce` function to multiply all the numbers in the range from 1 to `number_input + 1` and initializes the starting value as 1. The function takes an integer `number_input` as input and returns the factorial of that number as an integer.

### `factorial_while(number_input: int) -> int`

This function calculates the factorial of a given number using a while loop. It initializes a variable `result` as 1 and iterates through the numbers from `number_input` to 1, multiplying each number with `result` and decrementing `number_input` by 1 in each iteration. The function takes an integer `number_input` as input and returns the factorial of that number as an integer.

### `factorial_iterative(number_input: int) -> int`

This function calculates the factorial of a given number using an iterative approach. It initializes a variable `result` as 1 and iterates through the numbers from 1 to `number_input + 1`, multiplying each number with `result`. The function takes an integer `number_input` as input and returns the factorial of that number as an integer.

## Usage

To use the code, you can import the required modules and call the desired factorial function with a number as input. For example:

```python
import math
from functools import reduce
from operator import mul

# Calculate factorial using math.factorial
factorial_math_result = math.factorial(5)
print(factorial_math_result)

# Calculate factorial using recursive approach
factorial_recursive_result = factorial_recursive(5)
print(factorial_recursive_result)

# Calculate factorial using reduce function
factorial_reduce_result = factorial_reduce(5)
print(factorial_reduce_result)

# Calculate factorial using while loop
factorial_while_result = factorial_while(5)
print(factorial_while_result)

# Calculate factorial using iterative approach
factorial_iterative_result = factorial_iterative(5)
print(factorial_iterative_result)
```

Make sure to replace `5` with the desired number for which you want to calculate the factorial.

## Note

The code also includes a `try-except` block to handle any exceptions that may occur during the execution of the code. If an exception occurs, it will be printed to the console.

Please feel free to modify and use the code according to your requirements.