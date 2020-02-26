import sys
from copy import deepcopy
import math


def get_neighbors(pos):
    x = pos[0]
    y = pos[1]
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def find_portals():
    for pos1 in tuple(portal_labels):
        if pos1 not in portal_labels:
            continue

        portal_name = portal_labels[pos1]
        pos2 = ()
        for other_pos in get_neighbors(pos1):
            if other_pos not in portal_labels:
                continue
            pos2 = other_pos
            if pos2[0] < pos1[0] or pos2[1] < pos1[1]:
                portal_name = portal_labels[pos2] + portal_name
            else:
                portal_name += portal_labels[pos2]
            break
        del portal_labels[pos1]
        del portal_labels[pos2]

        if portal_name not in portal_to_locs:
            portal_to_locs[portal_name] = []

        for other_pos in (get_neighbors(pos1) + get_neighbors(pos2)):
            if other_pos in maze:
                portal_to_locs[portal_name].append(other_pos)
                locs_to_portals[other_pos] = portal_name
                break


def find_connections():
    for portal_pos in locs_to_portals:
        portal_name = locs_to_portals[portal_pos]
        if portal_name not in portal_connections:
            portal_connections[portal_name] = {}
        queue = [(portal_pos, 0)]
        visited = []
        while len(queue):
            pos, steps = queue.pop(0)
            visited.append(pos)

            if pos in locs_to_portals:
                other_portal_name = locs_to_portals[pos]
                portal_connections[portal_name][other_portal_name] = steps

            for next_pos in get_neighbors(pos):
                if next_pos not in maze or next_pos in visited:
                    continue
                queue.append((next_pos, steps + 1))


def solve(portal_name, visited):
    visited.append(portal_name)
    out = [math.inf]
    for name in portal_connections[portal_name]:
        steps = portal_connections[portal_name][name]
        if name == 'ZZ':
            out.append(steps)
            continue
        if name in visited:
            continue
        out.append(1 + steps + solve(name, deepcopy(visited)))
    return min(out)


with open(sys.argv[1]) as f:
    text = [[c for c in line.rstrip()] for line in f.readlines()]

maze = {}
portal_labels = {}
row = 0
for line in text:
    col = 0
    for c in line:
        if c == '.':
            maze[(row, col)] = 0
        elif c.isalpha():
            portal_labels[(row, col)] = c
        col += 1
    row += 1

portal_to_locs = {}
locs_to_portals = {}
find_portals()

portal_connections = {}
find_connections()

print(portal_connections)
print(solve('AA', []))
