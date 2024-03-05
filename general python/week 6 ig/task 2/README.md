# Timer Function Script

This Python script demonstrates a decorator that measures the execution time of a function.

## How to Use
1. Ensure you have Python installed on your system.
2. Run the script in a Python environment.
3. The script contains a `timer_func` decorator that calculates the execution time of a function.
4. The `long_time` function in the script is decorated with `@timer_func` to measure the execution time of a nested loop.
5. You can modify the `long_time` function to test the execution time of different operations.

## Script Execution
When you run the script, it will output the execution time of the `long_time` function in seconds.

## Example
```python
long_time(5)
