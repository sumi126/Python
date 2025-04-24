import random
while True:
    choose = input('Roll the dice? (y/n: )').lower()
    if choose == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'({dice1},{dice2})')
    elif choose == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid choice!')
