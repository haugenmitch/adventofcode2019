import sys
from computer import Computer
import matplotlib.pyplot as plt
from copy import deepcopy


def move(comp, position, step_count):
    step_count += 1
    for i in range(4):
        pos = deepcopy(position)
        if i == 0:
            pos[1] += 1
        elif i == 1:
            pos[1] -= 1
        elif i == 2:
            pos[0] -= 1
        else:
            pos[0] += 1
        if tuple(pos) in layout:
            continue
        new_comp = deepcopy(comp)
        new_comp.input(i+1)
        new_comp.run()
        out = new_comp.output()[0]
        layout[tuple(pos)] = out
        if out == 0:
            continue
        else:
            if out == 2:
                print(step_count)
            queue.append((new_comp, pos, step_count))


c = Computer(sys.argv[1])
layout = {(0, 0): 1}
queue = [(c, [0, 0], 0)]

while len(queue):
    item = queue.pop(0)
    move(item[0], item[1], item[2])

for key in layout:
    x = key[0]
    y = key[1]
    t = layout[key]
    k = 'k' if t == 0 else 'g' if t == 1 else 'y'
    a = 0.25 if t == 1 else 1
    plt.scatter(x, y, marker='s', color=k, alpha=a, s=100)
plt.show()

# plt.ion()
# plt.show()
# while not c.halted():
#     char = str(input('> '))
#     new_pos = deepcopy(pos)
#     if char == 'w':
#         c.input(1)
#         new_pos[1] += 1
#     elif char == 's':
#         c.input(2)
#         new_pos[1] -= 1
#     elif char == 'a':
#         c.input(3)
#         new_pos[0] -= 1
#     elif char == 'd':
#         c.input(4)
#         new_pos[0] += 1
#     else:
#         print(char)
#         continue
#
#     c.run()
#     status = c.output().pop(0)
#     if status == 0:
#         layout[tuple(new_pos)] = 0
#     elif status == 1:
#         pos = deepcopy(new_pos)
#         layout[tuple(pos)] = 1
#     elif status == 2:
#         pos = deepcopy(new_pos)
#         layout[tuple(pos)] = 2
#     else:
#
#         continue

# plt.clf()
# for key in layout:
#     x = key[0]
#     y = key[1]
#     t = layout[key]
#     k = 'k' if t == 0 else 'g' if t == 1 else 'y'
#     a = 0.25 if t == 1 else 1
#     plt.scatter(x, y, marker='s', color=k, alpha=a, s=100)
#     # plt.pause(0.001)
# plt.scatter(pos[0], pos[1], marker='o', color='r', s=100)
# plt.pause(0.001)
