import sys
from computer import Computer
import matplotlib.pyplot as plt

def turn(right):
    if right:
        return (direction + 1) % 4
    else:
        return (direction + 3) % 4

def move():
    if direction == 0:
        return pos[0], pos[1] + 1
    elif direction == 1:
        return pos[0] + 1, pos[1]
    elif direction == 2:
        return pos[0], pos[1] - 1
    else:
        return pos[0] - 1, pos[1]

with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

c = Computer(program)
c.run()

hull = {(0, 0): 1}
pos = (0, 0)
direction = 0
while not c.halted():
    val = 0
    if pos in hull:
        val = hull[pos]

    c.input(val)
    c.run()
    outputs = c.output()
    hull[pos] = outputs[0]
    direction = turn(outputs[1])
    pos = move()

points = [x for x in hull.keys() if hull[x] == 1]
plt.scatter(*zip(*points))
plt.show()

