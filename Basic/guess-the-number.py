import random
p1 = input("Enter the name of player1: ")
p2 = input("Enter the name of player2: ")
guess_number = random.randint(1,100)
count = 0
while True:
    count +=1
    try:
        if count % 2 == 0:
            guess = int(input(f"{p2} enter your guess number between 1 to 100: "))
        else:
           guess = int(input(f"{p1} enter your guess number between 1 to 100: "))
        if guess > guess_number:
           print(f'Please enter less than {guess}')
        elif guess < guess_number:
           print(f'Please enter more than {guess}')
        else:
           if count % 2 == 0:
                print(f'Congratulations {p2}! You are the winner.  ')
           else:
              print(f'Congratulations {p1}! You are the winner.  ')
           break
    except ValueError:
     print('Please enter valid number.')