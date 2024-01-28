# User Age Categorizer

## Description
This Python program collects user information, including their name and birth year, and categorizes their age into different age groups. It then saves the user information and age category in a CSV file.

## Installation
This program requires Python 3.x and the following dependencies:
- csv (comes pre-installed with Python)

To install the program, follow these steps:
1. Clone the repository: `git clone https://github.com/erfannaderi`
2. Navigate to the project directory: `cd user-age-categorizer`
3. Run the program: `python main.py`

## Usage
1. Run the program by executing the `user_age_categorizer.py` file.
2. Enter the user's information as prompted by the program.
3. To stop entering user information, enter '0' or leave the input blank.
4. The program will categorize the user's age into one of the following categories: 'kodak', 'nojavan', 'javan', or 'bozorg sal'.
5. The program will display the user's information and age category on the console.
6. The user information and age category will be saved in the 'users.csv' file.

## File Structure
- `main.py`: The main Python script that collects user information and categorizes their age.
- `users.csv`: The CSV file where the user information and age category are saved.

## Code Explanation
The program uses a while loop to continuously prompt the user for information until they enter '0' or leave the input blank. It then categorizes the user's age based on their birth year and stores the information in a dictionary. The user information and age category are displayed on the console and saved in a CSV file using the csv module.

