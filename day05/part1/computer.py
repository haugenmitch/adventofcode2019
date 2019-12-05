import sys


def decodeInstruction(instruction):
    opcode = int(str(instruction)[-2:])
    modesStr = str(instruction)[-3::-1]
    modes = []
    for i in range(numParams(opcode)):
        modes.append(0 if i >= len(modesStr) else int(modesStr[i]))

    return (opcode, modes)


def numParams(opcode):
    if opcode == 1 or opcode == 2:
        return 3
    elif opcode == 3 or opcode == 4:
        return 1
    else:
        return 0


with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

pc = 0
while pc < len(program):
    instruction = decodeInstruction(program[pc])
    pc = pc + len(instruction[1]) + 1
