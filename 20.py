names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Elon'
# print(names[1:])
# print(names)

# Program to find the largest number in a list
numbers = [23,455,22, 12, 500]

max = numbers[0]

for number in numbers:
    # max = max(max, number)
    if number > max:
      max = number
print(max)