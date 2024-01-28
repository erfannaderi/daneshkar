name = input("What is your name? ")
try:
    year_age = int(input("what year where you born? "))
    age = 1402 - year_age
    if 0 < age < 10:
        age_category = "kodak"
    elif 10 <= age < 15:
        age_category = "nojavan"
    elif 15 <= age < 30:
        age_category = "javan"
    elif 120 >= age >= 30:
        age_category = "bozorg sal "
    else:
        print("enter a valid year")
        age_category = 'WRONG YEAR'
except Exception as e:
    age_category = 'WRONG INPUT'
    print("Enter a valid INPUT")
    print(e)

if __name__ == "__main__":
    print(f"salam {name}, shoma {age_category} hastid.")
