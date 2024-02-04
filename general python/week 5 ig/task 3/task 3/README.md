# README: Matching User Input with Human Objects

This Python program allows you to match user input with a list of Human objects based on their name and age. The program prompts the user to enter the name and age of several humans and stores them in a list of Human objects. It then prompts the user to enter their own name and age and checks if there is a match in the list.

## Usage

1. Run the program in a Python environment.
2. Enter the name and age for each human when prompted.
3. Enter your own name and age when prompted.
4. The program will check if there is a match in the list and display the result.

## Example

```
Enter a name: Erfan
Enter an age: 25
Enter a name: Armin
Enter an age: 30
Enter a name: Hadi
Enter an age: 35
Enter a name: Karim
Enter an age: 40
Enter your name: Mmd
Enter your age: 30
Match found!
```

## Implementation Details

The program uses a `Human` class to represent each individual. The class has two attributes: `name` and `age`. The program creates a list called `humans` to store instances of the `Human` class.

The program prompts the user to enter the name and age for each human using the `input()` function. It then creates a `Human` object with the provided name and age and appends it to the `humans` list.

Next, the program prompts the user to enter their own name and age. It iterates over the `humans` list and checks if there is a match based on both name and age. If a match is found, the program sets the `match` variable to `True` and breaks out of the loop. Otherwise, it displays a "No match found" message and provides hints if the user's input for name or age is not empty.

The program uses a `try-except` block to catch any exceptions that may occur during execution and displays the error message if an exception occurs.

Feel free to modify the program to suit your specific needs. Enjoy matching user input with Human objects!