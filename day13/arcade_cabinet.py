import sys
from computer import Computer

with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

c = Computer(program)

score = -1
while not c.halted():
    c.run()
    board = {}
    out = c.output()
    paddle = -1
    ball = -1
    while len(out):
        x = out.pop(0)
        y = out.pop(0)
        t = out.pop(0)
        if x == -1 and y == 0:
            score = t
        else:
            if t == 3:
                paddle = x
            elif t == 4:
                ball = x
    c.input(-1 if ball < paddle else 1 if paddle < ball else 0)

print(score)
