# Dictionaries

customer = {
    "name": 'John smith',
    'age': '30',
    'is_verified': True,
    5: 'Five',
}

customer['name'] = 'Elon musk'
customer['dob'] = 'feb 14 1931'
# print(customer.get('dob', '12 jan 1981'))
# print(customer)

# Task:

phoneNumbers = input('Phone: ')

phone = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
}

output = ''
for number in phoneNumbers:
    output += phone.get(number, '!') + ' '

print(output.strip())