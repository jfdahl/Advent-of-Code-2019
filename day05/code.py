#!/usr/bin/env python3

#############
# Setup
#############
try:    # Get the input
    input_file = 'input.txt'
    with open(input_file, 'r') as fh:
        data = fh.readline()
        data = data.strip().split(',')
        data = [int(x) for x in data]
except FileNotFoundError:
    exit(f'The input file was not found: {input_file}')

def get_instruction(position: int) -> tuple:
    instruction = data[position]
    op = instruction % 100
    mode1 = instruction // 100 % 10
    mode2 = instruction // 1000 % 10
    # Thanks to Karl Uibo
    if op < 3: 
        param_count = 3
    elif op < 5: 
        param_count = 1
    elif op < 7:
        param_count = 2
    elif op < 9:
        param_count = 3
    else: 
        param_count = 0
    return op, [mode1, mode2], param_count

def get_parameters(position: int, count: int) -> list:
    parameters = data[position:position + count]
    return parameters

def get_values(params: list, param_modes: list) -> list:
    values = []
    for p, m in zip(params, param_modes):
        if m == 1:
            values.append(p)
        else:
            values.append(data[p])
    return values

def part1(data: list) -> None:
    buffer = 1 # System ID of the AC
    position = 0
    output = 0
    op, param_modes, param_count = get_instruction(position)
    while op in range(1,5):
        params = get_parameters(position + 1, param_count)
        if op == 3:
            data[params[0]] = buffer
            position += len(params) + 1
            op, param_modes, param_count = get_instruction(position)
            continue
        values = get_values(params, param_modes)
        
        if op == 4:
            output = values[0]
        
        if op == 1:
            data[params[2]] = values[0] + values[1]
        
        if op == 2:
            data[params[2]] = values[0] * values[1]
        
        position += len(params) + 1
        op, param_modes, param_count = get_instruction(position)
    print(f'Final Op Code: {op}\nOutput: {output}')

# part1(data)

def part2(data: list) -> None:
    buffer = 5 #int(input('Enter the system ID: ')) # System ID of the thermal radiator controller
    position = 0
    output = 0
    op, param_modes, param_count = get_instruction(position)
    while op in range(1,9):
        try:
            skip_normal_move = False
            params = get_parameters(position + 1, param_count)
            if op == 3:
                data[params[0]] = buffer
                position += param_count + 1
                op, param_modes, param_count = get_instruction(position)
                continue
            values = get_values(params, param_modes)
            if op == 4:
                output = values[0]
            
            if op == 1:
                data[params[2]] = values[0] + values[1]
            
            if op == 2:
                data[params[2]] = values[0] * values[1]
            
            if op == 5 and params[0] != 0:
                position = params[1]
                skip_normal_move = True
            
            if op == 6 and params[0] == 0:
                position = params[1]
                skip_normal_move = True

            if op == 7:
                if values[0] < values[1]: 
                    data[params[2]] = 1
                else:
                    data[params[2]] = 0

            if op == 8:
                if values[0] == values[1]: 
                    data[params[2]] = 1
                else:
                    data[params[2]] = 0

            if not skip_normal_move:
                position += param_count + 1
            op, param_modes, param_count = get_instruction(position)
            print(f'Position: {position}\nOp Code: {op}\nModes: {param_modes}\nParameters: {params}\nValues: {values}')
        except:
            print(f'ERROR: Position: {position}\nOp Code: {op}\nModes: {param_modes}\nParameters: {params}\nValues: {values}')
            break
    print(f'Final Op Code: {op}\nOutput: {output}')

print(data[:20])
part2(data)