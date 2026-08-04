class Dog:
    def __init__(self, name, age):
        self.name = name  # Property (Data)
        self.age = age    # Property (Data)

    def bark(self):       # Action (Method)
        print(f"{self.name} is {self.age} and says Woof!")

# Create an object (instance)
my_dog = Dog("Buddy", 3)

print(my_dog.name)  # Output: Buddy
my_dog.bark()       # Output: Buddy says Woof!


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Stella", 22)
print(f"The user's name is {user.name} and is {user.age} years old!")


class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"The user's name is {self.name} and is {self.age} years old!")

    def print_name(self):
        print(f"The user's name is {self.name}")

    def print_age(self):
        print(f"The user's age is {self.age}")


user1 = Users("Angela", 32)


user1.print_info()

user1.print_name()

user1.print_age()

