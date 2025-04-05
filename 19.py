# Nested loops

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# Challenge

numbers = [5, 2, 5, 2, 2]

# optimized code
# for i in numbers:
#     print('*' * i)

# less optimized code
for number in numbers:
    output = ''
    for i in range(number):
        output += '*'
    print(output)
