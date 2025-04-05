# Generating Random Values 
import random

# for i in range(3):
#     # print(random.random())
#     print(random.randint(10, 20))

# members = ['John', 'Mary', 'Bob', 'Mosh']
# print(random.choice(members))

# Task:

# Roll & dice

# Dice {class}
#   - roll() {tuple}


class Dice:
    def roll(self):
        # random_nums = (random.randint(1, 6), random.randint(7,12))
        # return random_nums
        first = random.randint(1, 6)
        second = random.randint(7,12)
        return first, second


dice = Dice()  
print(dice.roll())