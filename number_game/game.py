import random
def guess_game():
    comp_num = random.randint(1,101)
    print('Ok I have chosen a number! Try to guess it.')
    found = False
    attempts = 0
    while not found:
        num_guess = int(input('Number:'))
        if num_guess > comp_num:
            print(f'{num_guess}? No.. Try a smaller number..')
            attempts+=1
        elif num_guess < comp_num:
            print(f'{num_guess}? No.. Try a higher number..')
            attempts+=1
        else:
            attempts+=1
            print(f'You did it!! the number is indeed {comp_num}! only took you {attempts} attempts.')
            print("Thanks for playing! 🎉")
            found = True

guess_game()
