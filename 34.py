# Classes

# Types:

# Simple types 
# Numbers
# Strings
# Booleans

# ---

# Complex types 
# list 
# tuples
# dictionaries

# Name conventions of class starts from capital letters
# variables and funtion : lower case
# separate words: underscore
# naming classes:PascalNamingConvention: We do not separate using underscore(use title()):PascalCase: We capitalize first letter of every word



class Point:
    def move(self): # self is a special keyword added to method inside a class in python
        print('move')

    def draw(self):
        print('draw')

point1 = Point()
# point1.move()
point1.x = 10
point1.y = 20

# print(point1.x)

point2 = Point()
print(point2.x)

