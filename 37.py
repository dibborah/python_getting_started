# modules

import converters
from converters import lbs_to_kgs
from converters import kgs_to_lbs

import utils
from utils import find_max
# print(converters.lbs_to_kgs(100))
# print(converters.kgs_to_lbs(45))

# print(lbs_to_kgs(100))
# print(kgs_to_lbs(45))


# Task :

numbers = [33, 23, 11, 56, 400, 1000]
# print(utils.find_max(numbers))
# print(find_max(numbers))


# max is a reserved keyword in python
# max = find_max(numbers)
print(max(numbers))