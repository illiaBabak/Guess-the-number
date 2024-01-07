import random

EASY = 10
MEDIUM = 50
HARD = 100


def exit_check(input_text):
    return input_text.strip().lower() == "exit"


def select_difficulty():
    input_text = input(
        """Choose the difficulty:\n1 - easy(range from 1 to 10) \n2 - medium(range from 1 to 50)\n3 - hard(range from 1 to 100)\n"""
    )

    if exit_check(input_text):
        return

    try:
        complexity = int(input_text)
    except ValueError:
        print("Please enter a valid value.")
        select_difficulty()

    if complexity == 1:
        start_game(EASY)

    elif complexity == 2:
        start_game(MEDIUM)

    elif complexity == 3:
        start_game(HARD)

    else:
        print("Please enter a valid value.")
        select_difficulty()


def start_game(n):
    random_number = random.randint(1, n)
    guess(random_number)


def end_game():
    input_text = input("You won! Press enter to restart the game")

    if exit_check(input_text):
        return

    select_difficulty()


def guess(random_n):
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

        else:
            print("More")


input(
    """Welcome to the game "Guess the Number"!\nYour task is to guess the number guessed by the computer using logic. \nMinimize the number of attempts to become a winner!\nType "exit" to stop\n\nPress enter to start the game"""
)

select_difficulty()
