def print_with_word_decorator(word, decorator):
    print("-----------------------------\n")
    for sign in word:
        print(sign, end=decorator)
    print("\n\n-----------------------------")


def index_of_set(set, index):
    if len(set) < index:
        raise Exception("Index is too large.")
    return list(set)[index]


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
