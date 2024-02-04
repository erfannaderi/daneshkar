class Human:
    def __init__(self, name_class, age_class):
        self.name = name_class
        self.age = age_class


humans = list()
for _ in range(4):
    name = input("Enter a name: ")
    age = input("Enter an age: ")
    human = Human(name, age)
    humans.append(human)

match = False
while not match:
    try:
        user_name = input("Enter your name: ")
        user_age = input("Enter your age: ")
        for human in humans:
            if human.name == user_name and human.age == user_age:
                match = True
                break
        if match:
            print("Match found!")
        else:
            print("No match found.")
            if user_name != "":
                print("Hint: Check the spelling of your name.")
            if user_age != "":
                print("Hint: Check the format of your age.")
    except Exception as e:
        print(e)
