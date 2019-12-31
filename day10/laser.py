import math, sys

def angle_deg_true(tup):
    angle = math.atan2(tup[0], tup[1])
    if angle < 0:
        angle = angle + math.pi * 2
    return angle

with open(sys.argv[1]) as f:
    map = [l.strip() for l in f.readlines()]

asteroids = []
for i, row in enumerate(map):
    for j, c in enumerate(row):
        if c == '#':
            asteroids.append((j, i))

station = (19, 14)

beams = {}
for asteroid in asteroids:
    if asteroid[0] == station[0] and asteroid[1] == station[1]:
        continue
    x = asteroid[0] - station[0]
    y = station[1] - asteroid[1]
    gcd = abs(math.gcd(x, y))
    x = x / gcd
    y = y / gcd
    beam = (x, y)
    if beam in beams:
        beams[beam].append(gcd)
    else:
        beams[beam] = [gcd]

for beam in beams:
    beams[beam].sort()

beam_order = sorted(beams, key = angle_deg_true)

order = []
while len(beams) > 0:
    to_remove = []
    for beam in beam_order:
        gcd = beams[beam].pop(0)
        if len(beams[beam]) == 0:
            del beams[beam]
            to_remove.append(beam)
        asteroid_rel = (beam[0] * gcd, beam[1] * gcd)
        asteroid = (station[0] + asteroid_rel[0], station[1] - asteroid_rel[1])
        order.append(asteroid)
    beam_order = [x for x in beam_order if x not in to_remove]

print(order[199])