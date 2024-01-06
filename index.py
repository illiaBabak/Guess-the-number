import random

def start_game():
    random_number = random.randint(1, 100)
    guess(random_number)
    

def end_game():
    input('You won! Press enter to restart the game')
    start_game()
    

def guess(random_n):
    while True:
        input_text = input('Guess the number: ')
    
        try:
            number = int(input_text)
        except ValueError:
            print('Please enter a valid number.')
            continue

        if number == random_n:
            end_game()
            break

        elif number > random_n:
            print('Less')
     
        else:
            print('More')


input('''Welcome to the game "Guess the Number"!
Your task is to guess the number guessed by the computer using logic. 
Minimize the number of attempts to become a winner!
      
Press enter to start the game''')

start_game()