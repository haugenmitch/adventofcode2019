import sys
from computer import Computer
from copy import deepcopy

comp = Computer(sys.argv[1])

ship_width = 100
ship_height = 100

x = 55
y = 66
min_x = x
corner_x = {}
while True:
    c = deepcopy(comp)
    c.input([x, y])
    c.run()
    # o = c.output()[0]
    # print("x: %d  y: %d  o: %d" % (x, y, o))
    # if o:
    if c.output()[0]:  # in beam
        if x == min_x and (y - ship_height + 1) in corner_x:
            if x <= corner_x[(y - ship_height + 1)]:
                break
        x += 1
    else:
        if x == min_x:  # searching for start of next row
            x += 1
            min_x += 1
        else:  # past end of row
            # if x - min_x == 10:
            #     print("%d, %d" % (min_x, y))
            #     break
            corner_x[y] = x - ship_width
            y += 1
            x = min_x

final_y = y - ship_height + 1
final_x = corner_x[final_y]

print(final_x * 10000 + final_y)
