# Inheritance

class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('bark')

class Cat(Mammal):
    pass # telling python interpreter than pass this line: This is not an empty class

puppy = Dog()
# puppy.walk()
puppy.bark()

kitty = Cat()
kitty.walk()