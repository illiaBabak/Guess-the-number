import random

EASY = 10
MEDIUM = 50
HARD = 100

count = 1   


def exit_check(input_text):
    return input_text.strip().lower() == "exit"

def select_custom_difficulty():
    input_num1 = input("From: ")
    input_num2 = input("To: ")
    
    try:
        number1 = int(input_num1)
        number2 = int(input_num2)
    except ValueError:
        print("Please enter a valid values.")
        select_difficulty()
        
    if number1 > number2:
        print("First number can not be greater than second number")
        select_difficulty()
        
    start_game(number1, number2)


def select_difficulty():
    input_text = input(
        """Choose the difficulty:\n1 - easy(range from 1 to 10) \n2 - medium(range from 1 to 50)\n3 - hard(range from 1 to 100)\n4 - create your own range\n"""
    )
    
    if not input_text or exit_check(input_text):
        return

    try:
        complexity = int(input_text)
    except ValueError:
        print("Please enter a valid value.")
        select_difficulty()

    if complexity == 1:
        start_game(1, EASY)

    elif complexity == 2:
        start_game(1, MEDIUM)

    elif complexity == 3:
        start_game(1, HARD)
        
    elif complexity == 4:
        select_custom_difficulty()

    else:
        print("Please enter a valid value.")
        select_difficulty()


def start_game(first, second):
    global count
    count = 1
    random_number = random.randint(first, second)
    guess(random_number)


def end_game():
    input_text = input(f"You won! Number of attempts: {count}\nPress enter to restart the game")

    if exit_check(input_text):
        return

    select_difficulty()


def guess(random_n):
    global count
    while True:
        input_text = input("Guess the number: ")

        if exit_check(input_text):
            return

        try:
            number = int(input_text)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number == random_n:
            end_game()
            break

        elif number > random_n:
            print("Less")
            count += 1

        else:
            print("More")
            count += 1


input(
    """Welcome to the game "Guess the Number"!\nYour task is to guess the number guessed by the computer using logic. \nMinimize the number of attempts to become a winner!\nType "exit" to stop\n\nPress enter to start the game"""
)

select_difficulty()
