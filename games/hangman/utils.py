def print_with_word_decorator(word, decorator):
    print("-----------------------------\n")
    for sign in word:
        print(sign, end=decorator)
    print("\n\n-----------------------------")


def fill_breaks(list, sign):
    print("not implemented yet")


def index_of_set(set, index):
    try:
        sorted_list = list(set)
        sorted_list.sort()
        return sorted_list[index]
    except IndexError:
        print("Index must be smaller than set size")
        return -1


def concat_list_letters(char_list):
    word = ""
    for elem in char_list:
        word += elem
    return word


def split_word_to_list(word):
    char_list = []
    for letter in word:
        char_list.append(letter)
    return char_list


def get_mock_list(list, mock_char):
    mock_list = []

    for _ in list:
        mock_list.append(mock_char)

    return mock_list


def find_char_occurrences(expected_letter, word, info=False):
    char_occurrences = []

    for index, letter in enumerate(word):
        if expected_letter == letter:
            char_occurrences.append(index)

    if (info == True):
        print(char_occurrences)

    return char_occurrences
