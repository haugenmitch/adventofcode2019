import sys
from computer import Computer
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
            queue.append((new_comp, pos, step_count))
            if out == 2:
                print(step_count)
                return pos
    return None


def fill(position, step_count):
    step_count += 1
    n = (position[0], position[1] + 1)
    s = (position[0], position[1] - 1)
    w = (position[0] + 1, position[1])
    e = (position[0] - 1, position[1])
    nn = 0
    sn = 0
    wn = 0
    en = 0
    if n in layout and layout[n] != 0 and n not in flood:
        flood[n] = step_count
        nn = 1 + fill(n, step_count)
    if s in layout and layout[s] != 0 and s not in flood:
        flood[s] = step_count
        sn = 1 + fill(s, step_count)
    if w in layout and layout[w] != 0 and w not in flood:
        flood[w] = step_count
        wn = 1 + fill(w, step_count)
    if e in layout and layout[e] != 0 and e not in flood:
        flood[e] = step_count
        en = 1 + fill(e, step_count)
    return max(nn, sn, wn, en)


c = Computer(sys.argv[1])
layout = {(0, 0): 1}
queue = [(c, [0, 0], 0)]
oxygen_pos = []

while len(queue):
    item = queue.pop(0)
    r = move(item[0], item[1], item[2])
    if r != None:
        oxygen_pos = r

flood = {tuple(oxygen_pos): 0}

print(fill(tuple(oxygen_pos), 0))
