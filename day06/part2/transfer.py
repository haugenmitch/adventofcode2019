import sys


global orbits


def dist(o1, o2):
    path1 = path(o1)
    path2 = path(o2)

    for i,obj in enumerate(path1):
        if obj in path2:
            return path2.index(obj) + i - 2

    return -1


def path(obj):
    if obj not in orbits:
        return [obj]
    return [obj] + path(orbits[obj])


orbits = {}
with open(sys.argv[1]) as f:
    for line in f:
        orbit = line.strip().split(')')
        orbits[orbit[1]] = orbit[0]

print(dist('YOU', 'SAN'))
