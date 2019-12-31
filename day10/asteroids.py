import math, sys

with open(sys.argv[1]) as f:
    map = [l.strip() for l in f.readlines()]

asteroids = []
for i, row in enumerate(map):
    for j, c in enumerate(row):
        if c == '#':
            asteroids.append((j, i))

max = 0
pos = ()
for asteroid in asteroids:
    lines = []
    for other in asteroids:
        if asteroid[0] == other[0] and asteroid[1] == other[1]:
            continue
        x = asteroid[0] - other[0]
        y = asteroid[1] - other[1]
        gcd = abs(math.gcd(x, y))
        x = x / gcd
        y = y / gcd
        lines.append((x, y))
    l = len(list(set(lines)))
    if l > max:
        max = l
        pos = asteroid

print(max)
print(pos)