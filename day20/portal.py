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

        if portal_name == 'AA' or portal_name == 'ZZ':
            pass
        elif min(pos1[0], pos2[0]) == 0 or max(pos1[0], pos2[0]) == max_row \
                or min(pos1[1], pos2[1]) == 0 or max(pos1[1], pos2[1]) == max_col:
            portal_name += 'O'
        else:
            portal_name += 'I'

        del portal_labels[pos1]
        del portal_labels[pos2]

        for other_pos in (get_neighbors(pos1) + get_neighbors(pos2)):
            if other_pos in maze:
                locs_to_portals[other_pos] = portal_name
                break


def find_connections():
    for portal_pos in locs_to_portals:
        portal_name = locs_to_portals[portal_pos]
        portal_connections[portal_name] = {}
        if portal_name == 'ZZ':
            continue
        queue = [(portal_pos, 0)]
        visited = []
        while len(queue):
            pos, steps = queue.pop(0)
            visited.append(pos)

            if pos in locs_to_portals:
                other_portal_name = locs_to_portals[pos]
                if portal_name != other_portal_name and other_portal_name != 'AA':
                    portal_connections[portal_name][other_portal_name] = steps

            for next_pos in get_neighbors(pos):
                if next_pos not in maze or next_pos in visited:
                    continue
                queue.append((next_pos, steps + 1))


def solve(portal_name, level, visited):
    out = [math.inf]
    for name in portal_connections[portal_name]:
        steps = portal_connections[portal_name][name]
        if name == 'ZZ':
            if level == 0:
                out.append(steps)
            continue

        if name[2] == 'O' and level == 0:
            continue

        fingerprint = (portal_name, name, level)
        if fingerprint in visited:
            continue
        visited.append(fingerprint)
        is_inner = name[2] == 'I'
        new_level = level + (1 if is_inner else -1)
        if level > 25:  # don't let it recurse too deep (kinda inelegant)
            continue
        name = name[0:2] + ('O' if is_inner else 'I')
        out.append(1 + steps + solve(name, new_level, deepcopy(visited)))
    return min(out)


with open(sys.argv[1]) as f:
    text = [[c for c in line] for line in f.readlines()]

max_row = len(text) - 1
max_col = max([len(line) for line in text]) - 2

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

locs_to_portals = {}
find_portals()

portal_connections = {}
find_connections()

print(solve('AA', 0, []))
