import utils

dice_one = 0
dice_two = 0
dice_three = 0
dice_four = 0
dice_five = 0
dice_six = 0

number_of_tries = 0

dice_sum_throws = []
list_unit_dice_throws = []


def set_number_of_tries(probe_amount):
    global number_of_tries
    number_of_tries = probe_amount


def throws_dice(min=1, max=7):

    global list_unit_dice_throws

    for throws in range(number_of_tries):
        result_throw = utils.secret(min, max)

        if result_throw == 1:
            global dice_one
            dice_one += 1
            list_unit_dice_throws.append(1)
        elif result_throw == 2:
            global dice_two
            dice_two += 1
            list_unit_dice_throws.append(2)
        elif result_throw == 3:
            global dice_three
            dice_three += 1
            list_unit_dice_throws.append(3)
        elif result_throw == 4:
            global dice_four
            dice_four += 1
            list_unit_dice_throws.append(4)
        elif result_throw == 5:
            global dice_five
            dice_five += 1
            list_unit_dice_throws.append(5)
        elif result_throw == 6:
            global dice_six
            dice_six += 1
            list_unit_dice_throws.append(6)


def add_throws_sum_to_list():
    global dice_sum_throws

    dice_sum_throws.append(dice_one * 1)
    dice_sum_throws.append(dice_two * 2)
    dice_sum_throws.append(dice_three * 3)
    dice_sum_throws.append(dice_four * 4)
    dice_sum_throws.append(dice_five * 5)
    dice_sum_throws.append(dice_six * 6)

    return dice_sum_throws


def throws_avg():
    dice_sum_throws = add_throws_sum_to_list()
    return sum(dice_sum_throws) / number_of_tries


def format_and_print_result():
    print(f'Dice num{"Amount":>13}{"Sum":>17}')
    print("--------------------------------------")
    print(f'{1:>4}{dice_one:>17}{dice_one*1:>17}')
    print(f'{2:>4}{dice_two:>17}{dice_two*2:>17}')
    print(f'{3:>4}{dice_three:>17}{dice_three*3:>17}')
    print(f'{4:>4}{dice_four:>17}{dice_four*4:>17}')
    print(f'{5:>4}{dice_five:>17}{dice_five*5:>17}')
    print(f'{6:>4}{dice_six:>17}{dice_six*6:>17}')
    print("--------------------------------------")
    print("Average", throws_avg())
    print("Variance", utils.throws_variance(list_unit_dice_throws))
    print("Standard deviation", utils.throws_standard_deviation(
        list_unit_dice_throws))
