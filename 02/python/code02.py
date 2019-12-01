import sys
import math


def calculate_fuels(mass_list):
    modules = [get_needed_fuel(x) for x in mass_list]
    return sum(modules)


def get_needed_fuel(mass):
    new_mass = math.floor(mass/3)-2
    if new_mass > 0:
        return new_mass + get_needed_fuel(new_mass)
    else:
        return 0


# get lines
lines = [int(x) for x in sys.stdin.readlines()]

print("result is {}".format(calculate_fuels(lines)))
