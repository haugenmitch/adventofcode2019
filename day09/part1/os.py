import sys
from computer import Computer


with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

c = Computer(program, [2])
c.run()
print(c.output())
