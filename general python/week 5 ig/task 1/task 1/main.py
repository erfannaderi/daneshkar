class LivingBeing:
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def sleep(self):
        pass


class Human(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def work(self):
        print(f"{self.name} is working.")


class Animal(LivingBeing):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says woof!")


class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says meow!")


human = Human("erfan", 23)
human.eat()
human.sleep()
human.work()

dog = Dog("Buddy", "Golden Retriever")
dog.eat()
dog.sleep()
dog.make_sound()

cat = Cat("Whiskers", "Siamese")
cat.eat()
cat.sleep()
cat.make_sound()
