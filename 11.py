# Conditional if statements

is_hot = True
is_hot = False
is_cold = True
is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
# else:
#     print("It's a spring day")
# print("Enjoy your day")

# if is_hot:
#     print("It's a hot day")
# else:
#     print("It's a cold day")


# Task: 
price = 1000000
has_good_credit = True
# has_good_credit = False

# downpayment = 0

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f'The downpayment is: ${down_payment}')
        