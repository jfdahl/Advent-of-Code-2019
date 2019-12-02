#!/usr/bin/env python3

# Get the input as a list of ints
try:
    input_file = 'input.txt'
    with open(input_file, 'r') as fh:
        rows = fh.readline()
except FileNotFoundError:
    exit(f'The input file was not found: {input_file}')

# Define part 1 and part 2 code
def part1(data):
    return data

def part2(data):
    return data


# Test part 1
assert part1([1,0,0,0,99]) == [2,0,0,0,99]

# Copy input and execute part 1
assert part1(tmp)[0] == 3166704


# Execute part 2 (Copies are made in the function)
answer2 = part2(rows)
if answer2[0] == 19690720:
    print(100 * answer2[1] + answer2[2])
