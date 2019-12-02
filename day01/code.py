#!/usr/bin/env python3
import math

###############
# Setup
###############

try:
    input_file = 'input01.txt'
    with open(input_file, 'r') as fh:
        rows = fh.readlines()
    rows = [int(x) for x in rows]
except FileNotFoundError:
    exit(f'The input file was not found: {input_file}')

def how_much_fuel(mass):
    return math.floor(int(mass) / 3) - 2

###############
# Part 1
###############
def part1(modules):
    amount_of_fuel = 0

    for module in modules:
        amount_of_fuel += how_much_fuel(module)

    print(amount_of_fuel)

part1(rows) 
# Answer: 3429947

###############
# Part 2
###############

def part2(modules):
    amount_of_fuel = 0

    for module in modules:
        module_fuel = how_much_fuel(module)
        module_fuel_fuel = how_much_fuel(module_fuel)
        while module_fuel_fuel > 0:
            module_fuel += module_fuel_fuel
            module_fuel_fuel = how_much_fuel(module_fuel_fuel)
        amount_of_fuel += module_fuel

    print(amount_of_fuel)

part2(rows)
# Answer: 5142043
