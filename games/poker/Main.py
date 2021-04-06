from CardsDeck import CardsDeck
import itertools


def print_sorted_deck():
    print(CardsDeck())


def print_randomize_deck():
    randomize_deck = CardsDeck()
    randomize_deck.randomize_card_position()
    print(randomize_deck)
    

def print_random_card():
    randomize_deck = CardsDeck()
    randomize_deck.randomize_card_position()
    item = randomize_deck.get_random_card(0)
    print(item)

def check_points(cards_items):
    points = 0

    mylist = range(5)
    for x,y in itertools.combinations(mylist, 2):
        if(str(cards_items[x].value) == str(cards_items[y].value)):
            points += 1
            if str(cards_items[x].value) == "9":
                points *= 2
            elif str(cards_items[x].value) == "10":
                points *= 3
            elif str(cards_items[x].value) == "J":
                points *= 4
            elif str(cards_items[x].value) == "Q":
                points *= 5
            elif str(cards_items[x].value) == "K":
                points *= 6
            elif str(cards_items[x].value) == "As":
                points *= 7
            else:
                points *= 1

    return points

def get_random_deal_of_five_cards(): 
    randomize_deck = CardsDeck()
    randomize_deck.randomize_card_position()

    cards_items = []
    for i in range(5):
        cards_items.append(randomize_deck.get_random_card(i))
        print(cards_items[i].value, end=" ")
        if i == 4:
            print("\n")

    points = check_points(cards_items)
    return (cards_items, points)

def print_hr():
    print("--------------------------------------------------------------\n")


if __name__ == '__main__':
    # print_sorted_deck()
    # print_hr()
    # print_randomize_deck()
    # print_hr()
    # print_random_card()
    # print_hr()
    # cards_items = print_random_deal_of_five_cards()
    # print(cards_items)
    # for i in range(5):
    #     for j in range(5):
    #         if(cards_items[i].value == cards_items[j].value):
    #             print(cards_items[i].value)
    
    # mylist = range(5)
    # for x,y in itertools.combinations(mylist, 2):
    #     if(str(cards_items[x].value) == str(cards_items[y].value)):
    #         print(cards_items[x].value)

    # print(cards_items)

    kro = ()
    kro = get_random_deal_of_five_cards()
    print(kro)

    
    

    


