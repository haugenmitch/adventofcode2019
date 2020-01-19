from copy import deepcopy


def neighbors(tup):
    pos = tup[0]
    step = tup[1] + 1
    return [((pos[0]+1, pos[1]), step), ((pos[0]-1, pos[1]), step),
            ((pos[0], pos[1]+1), step), ((pos[0], pos[1]-1), step)]


def find_keys(tup, keys):
    queue = [tup]
    start_step = tup[1]
    checked = []
    paths = []
    while len(queue):
        tup = queue.pop()
        if tup[0] not in maze or tup[0] in checked:
            continue
        checked.append(tup[0])
        if 0 < max_dist < tup[1] - start_step:
            continue

        c = maze[tup[0]]
        if c == '.' or (97 <= ord(c) <= 122):
            queue += neighbors(tup)
            if 97 <= ord(c) <= 122 and ord(c) not in keys:
                new_keys = deepcopy(keys)
                new_keys[ord(c)] = tup[1]
                if len(new_keys.keys()) == num_keys:
                    print(tup[1])
                    return tup[1]
                else:
                    paths.append(find_keys(tup, new_keys))
        if 65 <= ord(c) <= 90 and (ord(c)+32) in keys:
            queue += neighbors(tup)

    return min(paths)


with open('maze.txt') as f:
    text = [[c for c in line.strip()] for line in f.readlines()]

start = ()
maze = {}
max_dist = -1
num_keys = 0
row = -1
for line in text:
    row += 1
    col = -1
    for c in line:
        col += 1
        if c == '@':
            start = (row, col)
            maze[(row, col)] = '.'
        elif c != '#':
            if 97 <= ord(c) <= 122:
                num_keys += 1
            maze[(row, col)] = c

print(find_keys((start, 0), {}))
