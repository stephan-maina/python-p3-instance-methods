class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"{self.name} says Hello World!")

    def walk(self):
        print(f"{self.name} is walking.")

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

# Example usage:
person1 = Person("Vincent", 21)
person2 = Person("Allan", 25)

person1.talk()
person1.walk()
person1.introduce()

person2.talk()
person2.walk()
person2.introduce()
