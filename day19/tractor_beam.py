import sys
from computer import Computer
from copy import deepcopy

c = Computer(sys.argv[1])

total = 0
for i in range(50):
    for j in range(50):
        d = deepcopy(c)
        d.input([i, j])
        d.run()
        total += d.output()[0]

print(total)
