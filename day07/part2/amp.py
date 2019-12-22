import sys
from itertools import permutations
from computer import Computer


with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

phases = list(permutations(list(range(5, 10))))

maxOutput = 0
maxPhase = []

for phase in phases:
    output = 0
    computers = [Computer(program, [p]) for p in phase]

    while not computers[4].halted():
        for computer in computers:
            computer.input(output)
            computer.run()
            output = computer.output()[0]

    if output > maxOutput:
        maxOutput = output
        maxPhase = phase
        print(str(phase) + " = " + str(output))
