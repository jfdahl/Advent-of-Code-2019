#!/usr/bin/env python3

#############
# Setup
#############
# Get the input
def get_data():
    try:
        data = {}
        with open('input.txt', 'r') as fh:
            for line in fh:
                line = line.strip().split(')')
                data[line[0]] = data.get(line[0], []) + [line[1]]
    except FileNotFoundError:
        exit(f'The input file was not found: {input_file}')
    return data

def get_children(parent: str, depth: int, path: str):
    '''Recursively walk down each orbital path and 
    update global variables to reflect count and paths.'''
    global orbit_count, path_san, path_you
    if parent == 'COM':
        path = parent
    else:
        path += f', {parent}'
    if parent == 'YOU': path_you = path
    if parent == 'SAN': path_san = path
    children = data.get(parent, None)
    if children is None: return
    depth += 1
    orbit_count += len(children) * depth
    for grandchild in children:
        get_children(grandchild, depth, path)

# Setup Global Variables (Yes, I know they are bad)
data = get_data()
orbit_count = 0
path_you = ''
path_san = ''

# Walk the orbits and create the paths
get_children('COM', depth=0, path='')
path_you = path_you.split(', ')
path_san = path_san.split(', ')

# Determine shared steps to COM
path_both = [step for step in path_you if step in path_san]
path_both2 = [step for step in path_san if step in path_you]
assert path_both == path_both2

# Remove shared steps to find the unique separation point
path_you = path_you[len(path_both):]
path_san = path_san[len(path_both):]

# Steps is one less than the number of positions
count_you = len(path_you) - 1
count_san = len(path_san) - 1

print(f'Total orbit count: {orbit_count}')
print(f'Traversal distance is {count_you} + {count_san} = {count_you + count_san}')
