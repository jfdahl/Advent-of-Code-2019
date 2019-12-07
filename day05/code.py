#!/usr/bin/env python3

#############
# Setup
#############
# try:    # Get the input
#     input_file = 'input.txt'
#     with open(input_file, 'r') as fh:
#         data = fh.readline()
#         data = data.strip().split(',')
#         data = [int(x) for x in data]
# except FileNotFoundError:
#     exit(f'The input file was not found: {input_file}')

data = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,40,71,224,1001,224,-111,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1102,66,6,225,1102,22,54,225,1,65,35,224,1001,224,-86,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,20,80,225,101,92,148,224,101,-162,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,60,225,1101,32,48,225,2,173,95,224,1001,224,-448,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,1001,91,16,224,101,-79,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,13,29,225,1101,71,70,225,1002,39,56,224,1001,224,-1232,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,14,59,225,102,38,143,224,1001,224,-494,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1102,30,28,224,1001,224,-840,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,344,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1007,677,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,389,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,677,226,224,1002,223,2,223,1006,224,419,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,434,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,449,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,539,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,554,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,569,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,584,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,599,101,1,223,223,1008,677,677,224,1002,223,2,223,1005,224,614,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,644,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,659,1001,223,1,223,1107,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]

def get_instruction(position: int) -> tuple:
    instruction = data[position]
    print(instruction)
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
                position = values[1]
                skip_normal_move = True
            
            if op == 6 and params[0] == 0:
                position = values[1]
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
            # print(f'Position: {position}\nOp Code: {op}\nModes: {param_modes}\nParameters: {params}\nValues: {values}')
        except:
            print(f'ERROR: Position: {position}\nOp Code: {op}\nModes: {param_modes}\nParameters: {params}\nValues: {values}')
            break
    print(f'Final Op Code: {op}\nOutput: {output}')

print(data[:20])
part2(data) #16694270
