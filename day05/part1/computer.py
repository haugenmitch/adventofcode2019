import sys


global program


def decodeInstruction(instruction):
    opcode = int(str(instruction)[-2:])
    modesStr = str(instruction)[-3::-1]
    modes = []
    for i in range(numParams(opcode)):
        modes.append(0 if i >= len(modesStr) else int(modesStr[i]))

    if len(modes):
        modes[-1] = 1

    return (opcode, modes)


def numParams(opcode):
    if opcode == 1 or opcode == 2:
        return 3
    elif opcode == 3 or opcode == 4:
        return 1
    else:
        return 0


def getParams(pc, modes):
    global program

    params = []
    pc = pc + 1
    for i,m in enumerate(modes):
        params.append(program[pc+i] if m == 1 else program[program[pc+i]])
    return params


def execute(opcode, params):
    global program

    if opcode == 1:
        program[params[2]] = params[0] + params[1]
    elif opcode == 2:
        program[params[2]] = params[0] * params[1]
    elif opcode == 3:
        program[params[0]] = int(input('Input: '))
    elif opcode == 4:
        print(program[params[0]])
    elif opcode == 99:
        print('EXIT')
        exit()
    else:
        print('Unknown opcode: ' + str(opcode))


global program
with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

pc = 0
while pc < len(program):
    instruction = decodeInstruction(program[pc])
    params = getParams(pc, instruction[1])
    execute(instruction[0], params)
    pc = pc + len(instruction[1]) + 1
