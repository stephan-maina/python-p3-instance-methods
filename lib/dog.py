class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.is_sitting = False

    def sit(self):
        self.is_sitting = True
        print(f"{self.name} is sitting.")

    def bark(self):
        print(f"{self.name} says Woof!")

    def fetch(self, item):
        print(f"{self.name} is fetching the {item}.")

# Example usage:
my_dog = Dog("Chess", "Golden Retriever")
my_dog.sit()
my_dog.bark()
my_dog.fetch("ball")
