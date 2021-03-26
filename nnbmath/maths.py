import math


def round_me(value, decimals):
    places = math.pow(10, decimals)
    value = (round(value * places) / places)
    return value
