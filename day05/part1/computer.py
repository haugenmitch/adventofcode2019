import sys


global program


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


def execute(pc, opcode, modes):
    if opcode == 1:
        add(pc, modes)
    elif opcode == 2:
        mult(pc, modes)
    elif opcode == 3:
        takeInput(pc)
    elif opcode == 4:
        output(pc, modes)
    elif opcode == 99:
        quit()
    else:
        unknown(pc, opcode, modes)


def add(pc, modes):
    global program
    val1 = program[pc+1] if modes[0] else program[program[pc+1]]
    val2 = program[pc+2] if modes[1] else program[program[pc+2]]
    program[program[pc+3]] = val1 + val2


def mult(pc, modes):
    global program
    val1 = program[pc+1] if modes[0] else program[program[pc+1]]
    val2 = program[pc+2] if modes[1] else program[program[pc+2]]
    program[program[pc+3]] = val1 * val2


def takeInput(pc):
    global program
    program[program[pc+1]] = int(input('Input: '))


def output(pc, modes):
    global program
    print(program[pc+1] if modes[0] else program[program[pc+1]])


def quit():
    print('EXIT')
    exit()


def unknow(pc, opcode, modes):
    print('Unknown opcode (pc/opcode/modes): ' + str(pc) + ' / ' + str(opcode) + ' / ' + str(modes))
    exit()


global program
with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

pc = 0
while pc < len(program):
    instruction = decodeInstruction(program[pc])
    execute(pc, instruction[0], instruction[1])
    pc = pc + len(instruction[1]) + 1
