import math
import sys
from copy import deepcopy


def add_path(char1, char2, path):
    current_paths = paths[char1][char2]
    ds = path[0]
    steps = path[1]
    for i in range(len(current_paths)):
        d = current_paths[i][0]
        s = current_paths[i][1]
        if ds == d:
            if steps < s:
                current_paths.remove(i)
                current_paths.append(path)
            return
    current_paths.append(path)


def find_paths(p):
    queue = [(0, points[p], 0)]
    master_visited = {}
    while len(queue):
        current = queue.pop(0)
        steps = current[0]
        position = current[1]
        ds = current[2]

        if position not in master_visited:
            master_visited[position] = []
        skip = False
        for previous_visit in master_visited[position]:
            d = previous_visit[0]
            s = previous_visit[1]
            if s <= steps and not d ^ (ds & d):
                skip = True
                break
        if skip:
            continue
        master_visited[position].append((ds, steps))

        char = maze[position]
        if (char.islower() or char is '@') and steps > 0:
            add_path(p, char, (ds, steps))
        elif char.isupper():
            ds += 1 << doors.index(char)

        x = position[0]
        y = position[1]
        steps += 1
        for i in range(4):
            if i == 0:
                new_pos = (x+1, y)
            elif i == 1:
                new_pos = (x, y+1)
            elif i == 2:
                new_pos = (x-1, y)
            else:
                new_pos = (x, y-1)

            if new_pos not in maze:
                continue
            queue.append((steps, new_pos, ds))


def solve(remaining_ks, acquired_ks, char):
    if remaining_ks == 0:
        return 0
    p = (char, remaining_ks)
    if p in solutions:
        return solutions[p]
    solutions[p] = math.inf
    for i in range(len(keys)):
        key = 1 << i
        if not key & remaining_ks:
            continue
        new_char = keys[i]
        possible_paths = paths[char][new_char]
        min_steps = math.inf
        for path in possible_paths:
            ds = path[0]
            steps = path[1]
            if ds ^ (acquired_ks & ds):
                continue
            min_steps = min(min_steps, steps)
        if min_steps == math.inf:
            continue
        min_steps += solve(remaining_ks ^ key, acquired_ks ^ key, new_char)
        solutions[p] = min(solutions[p], min_steps)

    return solutions[p]


with open(sys.argv[1]) as f:
    text = [[c for c in line.strip()] for line in f.readlines()]

start = ()
num_keys = 0
maze = {}
points = {}
doors = []
keys = []
row = -1
for line in text:
    row += 1
    col = -1
    for c in line:
        col += 1
        if c == '#':
            continue
        maze[(row, col)] = c
        pos = (row, col)
        if c == '@':
            start = pos
            points[c] = pos
        elif c.islower():
            points[c] = pos

keys = list(points.keys())
keys.sort()
keys.pop(0)
doors = [c.upper() for c in keys if c.isalpha()]

paths = {}
for point in points:
    paths[point] = {}
    for p2 in points:
        paths[point][p2] = []
    find_paths(point)

solutions = {}
print(solve((1 << len(keys))-1, 0, '@'))
