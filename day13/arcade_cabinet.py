import sys
from computer import Computer

with open(sys.argv[1]) as f:
    program = [int(n) for n in f.read().strip().split(',')]

c = Computer(program)
c.run()
out = c.output()

board = {}

while len(out):
    x = out.pop(0)
    y = out.pop(0)
    t = out.pop(0)
    board[(x, y)] = t

count = 0
for key in board:
    if board[key] == 2:
        count += 1

print(count)
