from CardsDeck import CardsDeck


def print_sorted_deck():
    print(CardsDeck())


def print_randomize_deck():
    randomize_deck = CardsDeck()
    randomize_deck.randomize_card_position()
    print(randomize_deck)


def print_hr():
    print("--------------------------------------------------------------\n")


if __name__ == '__main__':
    print_sorted_deck()
    print_hr()
    print_randomize_deck()
