# Comparison operator
# Comparison operators are used to compare two values. They return a boolean value (True or False).
# The comparison operators are: ==, !=, >, <, >=, <=
# == : Equal to
# != : Not equal to
# >  : Greater than
# <  : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

# temperature = 30
# temperature = 5

# if temperature > 30:
#     print("It's a hot day")
# elif temperature < 10:
#     print("It's a cold day")
# else:
#     print("It's neither hot nor cold")

# Task:

name = 'Dib Borah'
# name = 'Di'
# name = 'Dib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib BorahDib Borah'

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name can be maximum of 50 characters')
else:
    print("Name looks good!")