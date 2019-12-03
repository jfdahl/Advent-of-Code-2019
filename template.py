#!/usr/bin/env python3

#############
# Setup
#############
# Get the input
try:
    input_file = 'input.txt'
    with open(input_file, 'r') as fh:
        rows = fh.readlines()
except FileNotFoundError:
    exit(f'The input file was not found: {input_file}')

#############
# Part 1
#############
def part1(data):
    result = 0

    for item in data:
        pass # Do something

    return result

answer1 = part1(rows)
print(answer1)


#############
# Part 2
#############
def part2(data):
    result = 0

    for item in data:
        pass # Do something

    return result

answer2 = part2(rows)
print(answer2)
