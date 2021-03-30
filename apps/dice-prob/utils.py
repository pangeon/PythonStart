import random as rand
import statistics as stat
import secrets
import math

list_unit_dice_throws = []


def throws_variance(list_unit_dice_throws):
    dice_amount_throws = list_unit_dice_throws
    return round(stat.pvariance(dice_amount_throws), 3)


def throws_standard_deviation(list_unit_dice_throws):
    dice_amount_throws = list_unit_dice_throws
    return round(math.sqrt(stat.pvariance(dice_amount_throws)), 3)


def random_int(min, max):
    return rand.randrange(min, max)


def secret(min, max):
    return secrets.SystemRandom().randint(min, max)
