# Building a guessing game

guess_count = 0
secret_number = 9
guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     if guess == secret_number:
#         print('You win!')
#         break
#     guess_count+=1
# if guess != secret_number:
#     print('Sorry you failed!')

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    if guess == secret_number:
        print('You win!')
        break
    guess_count+=1
else:
    print('Sorry you failed!')