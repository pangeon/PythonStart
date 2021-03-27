def set_difficulty_level(difficulty_name):
    if difficulty_name == "HARD":
        amount_of_lives = 3
    elif difficulty_name == "MEDIUM":
        amount_of_lives = 5
    elif difficulty_name == "EASY":
        amount_of_lives = 8

    return amount_of_lives
