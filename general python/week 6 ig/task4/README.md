## Running the Python Script with Command-Line Argument

### Description

This Python script generates and prints numbers smaller than a given number specified as a command-line argument.

### Usage

To run the script with the provided command:

```
python main.py -n 10
```

This command will generate and print numbers smaller than 10.

### Script Details

- The script defines a function `generate_numbers_smaller_than(n)` that yields numbers from 1 up to `n-1`.
- It utilizes the `argparse` module to accept a command-line argument `-n` representing the number to generate numbers
  smaller than.
- If no number is provided, the script will display the help message.
- When a number is provided, it will generate and print numbers smaller than the given number.

Feel free to adjust the number specified after `-n` in the command to generate and print numbers smaller than your
desired value.