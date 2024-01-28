import csv
import time

users = []
while True:
    user_input = input("Enter 0 to stop or any other number to continue: ")

    if user_input == '0' or user_input == '':
        break

    try:
        user_input = int(user_input)
        name = input("What is your name? ")
        year_age = int(input("What year were you born? "))
        age = 1402 - year_age
        if 0 < age < 10:
            age_category = "kodak"
        elif 10 <= age < 15:
            age_category = "nojavan"
        elif 15 <= age < 30:
            age_category = "javan"
        elif 120 >= age >= 30:
            age_category = "bozorg sal"
        else:
            print("Enter a valid year")
            age_category = 'WRONG YEAR'
    except Exception as e:
        age_category = 'WRONG INPUT'
        name = "Error"
        print("Enter a valid year")
        print(e)

    user = {
        "name": name,
        "age_category": age_category
    }
    users.append(user)

for user in users:
    print("################################################################")
    print(f"Name: {user['name']}, Age Category: {user['age_category']}")
    print("**********************************************************")
    print(f"salam {name}, shoma {age_category} hastid.")

with open('users.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for user in users:
        writer.writerow({'Name': user['name'], 'Age Category': user['age_category']})

# Close the program after 20 seconds
time.sleep(20)
