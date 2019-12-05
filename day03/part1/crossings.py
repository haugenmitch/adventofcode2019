import sys

def intersection (verts, hors):
    cross = []
    for vtup in verts:
        for htup in hors:
            if htup[0] <= vtup[0] and vtup[0] <= htup[2] and vtup[1] <= htup[1] and htup[1] <= vtup[3]:
                cross.append((vtup[0], htup[1]))
    return cross

with open(sys.argv[1]) as f:
    wires = [line.strip() for line in f]

vertical = []
horizontal = []
for i in range(2):
    currPoint = [0, 0]
    wire = wires[i]
    vertSegs = []
    horzSegs = []

    for move in wire.split(','):
        direction = move[0]
        size = int(move[1:])

        newPoint = list(currPoint)
        if direction == 'U':
            newPoint[1] = currPoint[1] + size
            vertSegs.append((currPoint[0], currPoint[1], newPoint[0], newPoint[1]))
        elif direction == 'D':
            newPoint[1] = currPoint[1] - size
            vertSegs.append((newPoint[0], newPoint[1], currPoint[0], currPoint[1]))
        elif direction == 'L':
            newPoint[0] = currPoint[0] - size
            horzSegs.append((newPoint[0], newPoint[1], currPoint[0], currPoint[1]))
        else:
            newPoint[0] = currPoint[0] + size
            horzSegs.append((currPoint[0], currPoint[1], newPoint[0], newPoint[1]))

        currPoint = newPoint

    vertical.append(vertSegs)
    horizontal.append(horzSegs)

v1 = sorted(vertical[0], key=lambda tup: tup[0])
h1 = sorted(horizontal[0], key=lambda tup: tup[0])
v2 = sorted(vertical[1], key=lambda tup: tup[0])
h2 = sorted(horizontal[1], key=lambda tup: tup[0])

allCrosses = intersection(v1, h2) + intersection(v2, h1)

mini = 10000000

for coords in allCrosses:
    mini = min(mini, abs(coords[0]) + abs(coords[1]))

print(mini)
