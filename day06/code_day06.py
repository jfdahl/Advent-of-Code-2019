#!/usr/bin/env python3

#############
# Setup
#############
# Get the input
try:
    data = {}
    with open('input.txt', 'r') as fh:
        for line in fh:
            line = line.strip().split(')')
            data[line[0]] = data.get(line[0], []) + [line[1]]
except FileNotFoundError:
    exit(f'The input file was not found: {input_file}')

def get_children(parent: str, depth: int):
    global orbit_count
    depth += 1
    children = data.get(parent, None)
    if children is None:
        return
    count += len(children) * depth
    for grandchild in children:
        get_children(grandchild, depth)

orbit_count = 0
get_children('COM', 0)
print(orbit_count)


