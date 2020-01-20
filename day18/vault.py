from copy import deepcopy


def neighbors(tup):
    pos = tup[0]
    step = tup[1] + 1
    d = tup[2]
    return [((pos[0]+1, pos[1]), step, d), ((pos[0]-1, pos[1]), step, d),
            ((pos[0], pos[1]+1), step, d), ((pos[0], pos[1]-1), step, d)]


def find_paths(c, pos):
    nk = 0
    queue = [(pos, 0, [])]
    checked = []
    while nk < num_keys and len(queue):
        tup = queue.pop(0)
        pos = tup[0]
        step = tup[1]
        ds = tup[2]
        if pos in checked or pos not in maze:
            continue
        checked.append(pos)
        if pos in points:
            c_other = points[pos]
            paths[c][c_other] = (step, ds)
        elif pos in doors:
            nd = deepcopy(ds)
            nd.append(doors[pos])
            nd.sort()
            tup = (tup[0], tup[1], nd)
        queue += neighbors(tup)


def traverse(c, visited, dist):
    visited = deepcopy(visited)
    visited.append(c)
    visited.sort()
    out = []

    if len(visited) == 27:
        return dist

    for i in range(97, 123):
        if i in visited:
            continue
        req = paths[c][i]
        step = req[0]
        ds = req[1]
        if len([d for d in ds if d not in visited]):  # doors without keys
            continue
        out.append(traverse(i, visited, dist + step))

    return min(out)


with open('maze.txt') as f:
    text = [[c for c in line.strip()] for line in f.readlines()]

start = ()
num_keys = 0
maze = []
points = {}
doors = {}
row = -1
for line in text:
    row += 1
    col = -1
    for c in line:
        col += 1
        if c == '#':
            continue
        maze.append((row, col))
        n = ord(c)
        xy = (row, col)
        if n == 64 or 97 <= n <= 122:
            num_keys += 1
            points[xy] = n
            if n == 64:
                start = xy
        elif 65 <= n <= 90:
            doors[xy] = n + 32

paths = {}
for point in points:
    c = points[point]
    print(c)
    paths[c] = {}
    find_paths(c, point)

print(traverse(64, [], 0))
