#!/usr/bin/env python3
'''
'''

# Get the input
try:
    input_file = 'input.txt'
    with open(input_file, 'r') as fh:
        rows = fh.readlines()
except FileNotFoundError:
    exit(f'The input file was not found: {input_file}')

# Define part 1 and part 2 code
def part1(data):
    result = 0

    for item in data:
        pass # Do something

    return result

def part2(data):
    result = 0

    for item in data:
        pass # Do something

    return result


# Execute part 1 and part 2 code
answer1 = part1(rows)
print(answer1)

answer2 = part2(rows)
print(answer2)
