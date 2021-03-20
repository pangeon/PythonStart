def read_file_in_lines(reading_file):
    for line in reading_file.readlines():
        print(line.strip())


def write_line_in_file(file_to_writing, new_line, encoding):
    with open(file_to_writing, "a", encoding=encoding) as file_oject:
        file_oject.write(new_line + "\n")


def fill_and_split_line(first_word, second_word, size_empty_space):
    first_empty_space = size_empty_space - len(first_word)
    second_empty_space = size_empty_space - len(second_word)

    x = 0
    for x in range(first_empty_space):
        first_word += " "
        x += 1

    for x in range(second_empty_space):
        second_word += " "
        x += 1

    return "| " + first_word + "| " + second_word + "| "
