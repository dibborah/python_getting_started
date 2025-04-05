# keyword arguements

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome abroad!')


print('Start')
# greet_user('Musk', 'Elon')# positional arguements: Position of order matters
# greet_user(last_name='Musk', first_name='Elon')# keyword arguements: Position of order does not matters
greet_user('Musk', last_name='Elon')# keyword arguements: Position of order does not matters
print('Finish')

#Note: always use positional arguements first than use keyword arguements

# No readability 
# calc_cost(50, 5, 0.1) # No readability : Once cannot understand what the parameter are all about

# For better readability we use keyword arguements
# calc_cost(total=50, shipping=5, discout=0.1)