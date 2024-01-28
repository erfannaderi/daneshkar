# README

## Introduction

This is a Python project that determines the age category of a person based on their birth year. It prompts the user to enter their name and birth year, and then calculates their age and assigns them to an age category. The project demonstrates the usage of the `if __name__ == '__main__':` statement in Python.

## Usage

To run the program, execute the following command in your Python environment:

```bash
python main.py
```

The program will prompt you to enter your name and birth year. After entering the required information, it will calculate your age and assign you to an age category. The program will then display a greeting message with your name and age category.

## Code Explanation

The code begins by prompting the user to enter their name and birth year. The birth year is converted to an integer using the `int()` function. The age is calculated by subtracting the birth year from the current year (1402 in this case).

The program then uses a series of `if` and `elif` statements to determine the age category based on the calculated age. The age categories are defined as follows:

- `kodak`: Age is between 0 and 10 (exclusive).
- `nojavan`: Age is between 10 and 15 (exclusive).
- `javan`: Age is between 15 and 30 (exclusive).
- `bozorg sal`: Age is between 30 and 120 (inclusive).

If the age falls outside of these ranges, an error message is displayed and the age category is set to `'WRONG YEAR'`.

Finally, the program checks if the script is being run as the main module using the `if __name__ == '__main__':` statement. If it is, the program displays a greeting message with the user's name and age category using an f-string.

## Conclusion

This project demonstrates how to use the `if __name__ == '__main__':` statement in Python to execute code only when the script is run as the main module. It also showcases the usage of conditional statements and user input in Python. Feel free to explore the code and modify it according to your needs.