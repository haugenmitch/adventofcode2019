import sys
from computer import Computer

c = Computer(sys.argv[1])
c.run()
vals = c.output()
row = 0
column = 0
scaffolding = {}
for n in vals:
    c = chr(n)
    if c == '#':
        scaffolding[(row, column)] = row * column
    elif c == '.':
        pass
    elif c == '\n':
        row += 1
        column = 0
        continue
    else:
        pass
    column += 1

total = 0
for key in scaffolding:
    row = key[0]
    col = key[1]
    if (row-1, col) in scaffolding and (row+1, col) in scaffolding and (row, col-1) in scaffolding and (row, col+1) in scaffolding:
        total += scaffolding[key]

print(total)
