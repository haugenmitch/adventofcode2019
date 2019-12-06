import sys


global orbits, orbitHeight


def calcOrbitHeight(orbit):
    if orbit[1] not in orbitHeight:
        calcOrbitHeight((orbit[1], orbits[orbit[1]]))

    orbitHeight[orbit[0]] = orbitHeight[orbit[1]] + 1


orbits = {}
with open(sys.argv[1]) as f:
    for line in f:
        orbit = line.strip().split(')')
        orbits[orbit[1]] = orbit[0]

orbitHeight = {}
orbitHeight['COM'] = 0

for orbit in orbits.items():
    calcOrbitHeight(orbit)

print(sum(orbitHeight.values()))
