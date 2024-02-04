# README.md

## Random Winner Selector

This Python program randomly selects a winner from a list of 1000 people. It generates random human objects with attributes such as first name, last name, age, address, and date of birth. It then selects a winner from the generated list and displays their information.

## Usage

To use this program, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone or download the program files from the repository.
3. Open the terminal or command prompt and navigate to the program directory.
4. Run the following command to execute the program:

   ```
   python main.py
   ```

5. The program will randomly select a winner from the list of 1000 people and display their information, including first name, last name, age, address, and date of birth.

## Dependencies

This program requires the following dependencies:

- Python (version 3.0 or above)
- Random module (built-in)
- String module (built-in)

## Customization

You can customize the program by modifying the following parameters:

- Number of people: By changing the range in the for loop, you can generate a different number of people. For example, to generate 100 people, change the range to `range(100)`.
- Attribute lengths: By modifying the `random.randint()` function calls, you can change the length of attributes such as first name and last name. For example, to generate first names with a length between 3 and 10 characters, change the `random.randint(1, len(alphabets))` calls to `random.randint(3, 10)`.

## Example Output

Here is an example output of the program:

```
Winner:
First Name: John
Last Name: Doe
Age: 35
Address: Address123
Date of Birth: 1985
```