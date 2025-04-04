# logical operators
# Logical operators are used to combine conditional statements

# and, or, not
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true


# Example of and operator 
# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit: 
#     print(f'Elligible for loan')
# else:
#     print("Not elligible for loan")

# -------- x -------

# Example of or operator
# has_high_income = False
# has_good_credit = True

# if has_good_credit or has_good_credit:
#     print('Elligible for loan')

# -------- x -------

# Example of the not operator
has_good_credit = True
has_criminal_record = False
# has_criminal_record = True

if has_good_credit and not has_criminal_record:
  print('Elligible for loan')