import utils
import visual
import sys

word_to_guess = "yellow"
hint = "Name of color"

word_list = []
word_list = utils.get_mock_list(word_to_guess, "_")

used_letters = []

version = 1.0


def print_welcome_header():
    print("Welcome in hangman " + str(version) + " by Kamil Cecherz\n")


def print_question():
    print("Hint: " + hint + " <> Number of letters: " + str(len(word_to_guess)))
    print("You try guess letter in the word.\n")


def print_winner_info():
    print("You're winner !")
    print("The word you were looking for is:")
    utils.print_with_word_decorator(word_to_guess, ' ')


def start():
    print_welcome_header()
    print_question()

    lives = 5

    while True:
        user_answer = input("\nEnter correct letter in this word\n")
        used_letters.append(user_answer)

        found_indexes = utils.find_char_occurrences(user_answer, word_to_guess)

        if len(found_indexes) == 0:
            print("\nLetter not exist in this word\n")
            lives -= 1

            if lives == 0:
                utils.print_with_word_decorator("GAME OVER", ' ')
                print(visual.image_end)
                sys.exit(0)
        else:
            for index in found_indexes:
                word_list[index] = user_answer

        if utils.concat_list_letters(word_list) == word_to_guess:
            print_winner_info()
            sys.exit(0)
        else:
            print("\nLIVES: " + str(lives) + "\n")
            print("Used letters:", used_letters)
            print(word_list)


start()
