#!/usr/bin/env python3

# Get the input as a list of ints
try:
    input_file = 'input.txt'
    with open(input_file, 'r') as fh:
        data = fh.readlines()
    data = [x.strip().split(',') for x in data]
except FileNotFoundError:
    exit(f'The input file was not found: {input_file}')

   
def step(position, direction):
    '''Given a list of coordinates and a direction,
    determine the coordinates of the next step'''
    if direction == 'R':
        position[0] += 1
    elif direction == 'L':
        position[0] -= 1
    elif direction == 'U':
        position[1] += 1
    elif direction == 'D':
        position[1] -= 1
    return position

def walk(position, movement):
    '''Given a tuple of starting coordinates and a movement command,
    determine each step in the movement.'''
    direction = movement[0]
    distance = int(movement[1:])
    steps = [position]
    while distance > 0:
        position = tuple(step(list(position), direction))
        steps.append(position)
        distance -= 1
    return steps[1:]
    
def trace_wire(moves):
    steps = [(0,0)]
    for move in moves:
        steps.extend(walk(steps[-1], move))
    return steps[1:]

def calculate_distance(position):
    return abs(position[0]) + abs(position[1])

def closest_intersection(intersections):
    intersection = min([(calculate_distance(x), x) for x in intersections])
    print(intersection[0])


# Define part 1 and part 2 code
def part1(data):
    wire1_moves = data[0]
    wire1_positions = trace_wire(wire1_moves)
    set1 = set(wire1_positions)

    wire2_moves = data[1]
    wire2_positions = trace_wire(wire2_moves)
    set2 = set(wire2_positions)

    intersections = list(set1.intersection(set2))
    print(intersections)

    closest_intersection(intersections)
    return None

# # Test 0 = 6
# wire1 = 'R8,U5,L5,D3'.split(',')
# wire2 = 'U7,R6,D4,L4'.split(',')
# part1([wire1, wire2])

# # Test 1 = 159
# wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
# wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
# part1([wire1, wire2])

# # Test 2 = 135
# wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
# wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
# part1([wire1, wire2])

# part1(data)


def part2(data):
    wire1_moves = data[0]
    wire1_positions = trace_wire(wire1_moves)
    set1 = set(wire1_positions)

    wire2_moves = data[1]
    wire2_positions = trace_wire(wire2_moves)
    set2 = set(wire2_positions)

    intersections = list(set1.intersection(set2))
    distances = []
    for intersection in intersections:
        dist1 = wire1_positions.index(intersection) + 1 # Correct for a zero-based list
        dist2 = wire2_positions.index(intersection) + 1 # Correct for a zero-based list
        distances.append(dist1 + dist2)
    print(min(distances))
    return None


# Test 0 = 30
wire1 = 'R8,U5,L5,D3'.split(',')
wire2 = 'U7,R6,D4,L4'.split(',')
part2([wire1, wire2])

# Test 1 = 610
wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
part2([wire1, wire2])

# Test 2 = 410
wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
part2([wire1, wire2])

part2(data)