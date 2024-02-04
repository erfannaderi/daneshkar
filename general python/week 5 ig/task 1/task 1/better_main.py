from dataclasses import dataclass


@dataclass
class LivingBeing:
    name: str

    def eat(self) -> None:
        pass

    def sleep(self) -> None:
        pass


@dataclass
class Human(LivingBeing):
    age: int

    def eat(self) -> None:
        print(f"{self.name} is eating.")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping.")

    def work(self) -> None:
        print(f"{self.name} is working.")


@dataclass
class Animal(LivingBeing):
    species: str

    def eat(self) -> None:
        print(f"{self.name} is eating.")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping.")

    def make_sound(self) -> None:
        pass


@dataclass
class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says woof!")


@dataclass
class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says meow!")


# Testing the classes
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
