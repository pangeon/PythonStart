import utils
import visual
import settings
import sys

word_to_guess = "yellow and black"
hint = "Name of color"

word_list = []
word_list = utils.get_mock_list(word_to_guess, "_")
difficulty_level_names = {"EASY", "MEDIUM", "HARD"}

used_letters = []

version = "1.1.1"


def print_welcome_header():
    print("Welcome in hangman " + str(version) + " by Kamil Cecherz\n")


def print_question():
    print("Hint: " + hint + " <> Number of letters: " + str(len(word_to_guess)))
    print("You try guess letter in the word.")
    print("If you want use whitespace click once space button.\n")


def print_winner_info():
    print("You're winner !")
    print("The word you were looking for is:")
    utils.print_with_word_decorator(word_to_guess, ' ')


def print_difficulty_level_info():
    print("Set game diffilculty\n")
    print("1 -- EASY\n")
    print("2 -- MEDIUM\n")
    print("3 -- HARD\n")


def start():
    print_welcome_header()
    print_question()

    print_difficulty_level_info()

    user_level_choice = int(input("Enter the number: "))

    # EASY, MEDIUM, HARD
    difficulty_name = utils.index_of_set(difficulty_level_names, 1)
    lives = settings.set_difficulty_level(difficulty_name)

    while True:
        user_answer = input("\nEnter correct letter in this word\n")
        used_letters.append(user_answer)

        found_indexes = utils.find_char_occurrences(user_answer, word_to_guess)

        if len(found_indexes) == 0:
            print("\nLetter not exist in this word\n")
            lives -= 1

            visual.show_stage_image(lives)

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
