import datetime

import text_utils
import mock

file_name = "memes.txt"
enconding = "utf-8"
version = 1.0


def user_choice():
    return int(input("Choose option \n" +
                     "\n 1 - open saved memes"
                     "\n 2 - add new meme"
                     "\n 3 - exit"
                     "\n"
                     ))


def read_memes_base():
    memes_base = open(file_name, "r", encoding=enconding)
    text_utils.read_file_in_lines(memes_base)


def write_new_mem_to_base():
    print("Write your new mem\n")
    eng_meaning = input("Write english word\n")
    pol_meaning = input("Translate word to polish\n")
    mem_content = text_utils.fill_and_split_line(eng_meaning, pol_meaning, 15)

    date = datetime.date.today()
    mem_date_and_content = mem_content + str(date)

    text_utils.write_line_in_file(file_name, mem_date_and_content, enconding)


def exit_message():
    print("You are leaving the programme.")


def error_message():
    print("Error. Unsupported operation !")


def welcome_message():
    print("Welcome in eng-meme " + str(version) + " by Kamil Cecherz")


def start():
    welcome_message()
    option = 0
    while option != 3:
        option = user_choice()
        if option == 1:
            read_memes_base()
        elif option == 2:
            write_new_mem_to_base()
        elif option == 3:
            exit_message()
        else:
            error_message()


start()
