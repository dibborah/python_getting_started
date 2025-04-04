# Weight converter Program

# This program converts weight from pounds to kilograms and vice versa.
# The user is prompted to enter the weight and the unit (pounds or kilograms).
# The program then performs the conversion and displays the result.
# The conversion factors are:

# 1 pound = 0.45 kg

weight = input('Weight: ')
unit = input('(L)bs or (K)g: ').lower()

if unit == 'l':
    print(f'You are {float(weight) * 0.45} kilos')
else:
    # print(f'You are {float(weight) * 2.2} pounds')
    print(f'You are {float(weight) / 0.45} pounds')


# string = 'hello world'
# print(str.lower(string))
# print(str.upper(string))
# print('hello world'.upper())