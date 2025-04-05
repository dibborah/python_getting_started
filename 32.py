# Exceptions
# Or Error handling

# age = int(input('Age: '))
# print(age)

try:
    age = int(input('Age: '))
    income = 320000
    risk = income / age
    print(age)
except ValueError: # This is the exception we are taking about: Basically error handling
    print('Invalid value')
except ZeroDivisionError:
    print('Invalid division')