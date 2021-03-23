version = 1.0
lives = 5

word_to_guess = "yellow"
hint = "Name of color"


def print_welcome_header():
    print("Welcome in hangman " + str(version) + " by Kamil Cecherz\n")


def print_question():
    print("Hint: " + hint + " <> Number of letters: " + str(len(word_to_guess)))
    print("You try guess letter in the word.\n")


def get_empty_game_board():
    game_board = []
    amount_of_letters = len(word_to_guess)

    for _ in range(amount_of_letters):
        game_board.append("_")

    return game_board


def get_filled_game_board():
    game_board = []

    for index in word_to_guess:
        game_board.append(index)

    return game_board


def show_lives_amount():
    print("LIVES: " + str(lives) + "\n")


def user_guess_the_word():
    print("not implemented yet")


def start():

    print_welcome_header()
    print_question()

    show_lives_amount()


start()
