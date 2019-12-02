#!/usr/bin/env python3

# Get the input as a list of ints
try:
    input_file = 'input.txt'
    with open(input_file, 'r') as fh:
        rows = fh.readline()
    rows = rows.strip().split(',')
    rows = [int(x) for x in rows]
except FileNotFoundError:
    exit(f'The input file was not found: {input_file}')

# Define part 1 and part 2 code
def part1(data):
    position = 0
    while position < len(data):
        op = data[position]
        if op == 99:
            break
        a = data[position + 1]
        b = data[position + 2]
        c = data[position + 3]

        if op == 1:
            data[c] = data[a] + data[b]
        elif op == 2:
            data[c] = data[a] * data[b]
        else:
            position += 1
            continue
        
        position += 4
    return data

def part2(data):
    nouns = range(100)
    verbs = range(100)
    
    for verb in verbs:
        for noun in nouns:
            tmp = data[:]
            tmp[1] = noun
            tmp[2] = verb
            answer = part1(tmp)
            if answer[0] == 19690720:
                return tmp[:3]
    return tmp


# Test part 1
assert part1([1,0,0,0,99]) == [2,0,0,0,99]
assert part1([2,3,0,3,99]) == [2,3,0,6,99]
assert part1([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert part1([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

# Copy input and execute part 1
tmp = rows[:]
tmp[1] = 12
tmp[2] = 2
assert part1(tmp)[0] == 3166704


# Execute part 2 (Copies are made in the function)
answer2 = part2(rows)
if answer2[0] == 19690720:
    print(100 * answer2[1] + answer2[2])
