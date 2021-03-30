import rand_dice_gen as r_dice
import secret_dice_gen as s_dice

probe_amount = 1_000_000

print("---------- Random dice test ----------")
r_dice.set_number_of_tries(probe_amount)
r_dice.throws_dice()
r_dice.format_and_print_result()

print("---------- Secret dice test ----------")
s_dice.set_number_of_tries(probe_amount)
s_dice.throws_dice()
s_dice.format_and_print_result()
