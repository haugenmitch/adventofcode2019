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
    queue = [(0, points[p], 0, [])]
    master_visited = {}
    while len(queue):
        # print(len(queue))
        current = queue.pop(0)
        steps = current[0]
        position = current[1]
        ds = current[2]
        visited = deepcopy(current[3])

        if (position not in maze) or (position in visited):
            continue
        if position not in master_visited:
            master_visited[position] = []
        skip = False
        for previous_visit in master_visited[position]:
            d = previous_visit[0]
            s = previous_visit[1]
            if s < steps and not ds ^ (ds & d):
                skip = True
                break
        if skip:
            continue
        master_visited[position].append((ds, steps))
        visited.append(position)

        char = maze[position]
        if (char.islower() or char is '@') and steps > 0:
            add_path(p, char, (ds, steps))
        elif char.isupper():
            ds += 1 << doors.index(char)

        x = position[0]
        y = position[1]
        steps += 1
        queue.append((steps, (x+1, y), ds, visited))
        queue.append((steps, (x, y+1), ds, visited))
        queue.append((steps, (x-1, y), ds, visited))
        queue.append((steps, (x, y-1), ds, visited))


# def solve(char, ps, ks):
#     ps = deepcopy(ps)
#     for key in ps:
#         del ps[key][char]
#
#     if char != '@':
#         ks += 1 << keys.index(char)
#     out = []
#     for key in ps[char]:
#         min_steps = 100000
#         for tup in ps[char][key]:
#             ds = tup[0]
#             steps = tup[1]
#             if steps < min_steps and not (ds ^ (ds & ks)):
#                 min_steps = steps
#         if min_steps != 100000:
#             out.append(min_steps + solve(key, ps, ks))
#
#     if len(out):
#         return min(out)
#
#     return 0


def key_id(ks):
    out = 0
    for key in ks:
        out += 1 << keys.index(key)
    return out


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
    print(p)
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

print(points)

paths = {}
for point in points:
    print(point)
    paths[point] = {}
    for p2 in points:
        paths[point][p2] = []
    find_paths(point)

solutions = {}
print(solve((1 << len(keys))-1, 0, '@'))
