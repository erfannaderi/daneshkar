import random
import string


class Human:
    def __init__(self, first_name_class, last_name_class, age_class, address_class, date_of_birth_class):
        self.first_name = first_name_class
        self.last_name = last_name_class
        self.age = age_class
        self.address = address_class
        self.date_of_birth = date_of_birth_class


alphabets = list(string.ascii_letters)
humans = dict()

for i in range(1000):
    first_name = ''.join([random.choice(alphabets) for _ in range(random.randint(1, len(alphabets)))])
    last_name = ''.join([random.choice(alphabets) for _ in range(random.randint(1, len(alphabets)))])
    age = random.randint(1, 100)
    address = "Address" + str(i)
    date_of_birth = random.randint(1900, 2006)
    human = Human(first_name, last_name, age, address, date_of_birth)
    humans[i] = human

winner_index = random.choice(list(humans.keys()))
winner = humans[winner_index]

print("Winner:")
print("First Name:", winner.first_name)
print("Last Name:", winner.last_name)
print("Age:", winner.age)
print("Address:", winner.address)
print("Date of Birth:", winner.date_of_birth)
