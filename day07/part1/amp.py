import sys
from itertools import permutations
from computer import Computer


with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

phases = list(permutations(list(range(5))))

maxOutput = 0
maxPhase = []

for phase in phases:
    output = 0
    for i in range(5):
        c = Computer(program, [phase[i], output])
        output = c.run()[0]

    if output > maxOutput:
        maxOutput = output
        maxPhase = phase
        print(str(phase) + " = " + str(output))
