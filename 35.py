# constructors

# A constructor is a function that gets called when creating an object

class Point:
    def __init__(self, x, y):# We refer to this __init__ method as constructor # self is the reference to the current object
        self.x = x
        self.y = y
    
    def move(self): # self is a special keyword added to method inside a class in python
        print('move')

    def draw(self):
        print('draw')


# point1 = Point(x, y)
point1 = Point(10, 20)
# print(point1.y, point1.x)

point1.x = 100
# print(point1.x)


# Task: 

# Person
#   - name
#   - talk()


# Solution
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        # print('talk!')
        print(f'Hi, I am {self.name}!')


kriya = Person('Kriya Saikia')

print(kriya.name)
kriya.talk()


arpan = Person('Arpan Borah')

print(arpan.name)
arpan.talk()