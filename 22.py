# Lists methods 

# numbers = [2, 1, 5, 7, 5, 4, 5]

# append()
# insert()
# index()
# pop()
# remove()
# clear()
# count()
# sort()
# reverse()
# copy()

# numbers.append(100)
# print(numbers)

# numbers.insert(1, 600)
# print(numbers)

# print(numbers.index(5))

# print(numbers.pop())
# print(numbers)

# print(numbers.remove(5)) # Doesnot return anything( None will be printed)
# print(numbers)

# print(numbers.clear()) # Doesnot return anything( None will be printed)
# print(numbers)

# print(numbers.count(5))

# print(numbers.sort()) # Doesnot return anything( None will be printed)
# print(numbers)

# print(numbers.reverse()) # Doesnot return anything( None will be printed)
# print(numbers)

# print(numbers)
# numbers2 = numbers.copy()
# numbers.sort()

# print(numbers)
# print(numbers2)

# Task: 

# Write a program to remove the duplicated in a list 
numbers = [3,3,11,5,5,5,6,7]

# numbers.sort()

# for number in numbers:
#     if numbers.count(number) > 1:
#         numbers.remove(number)
# print(numbers)

uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)