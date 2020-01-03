from moon import Moon
from moon2 import Moon2
from math import gcd


def state(moons):
    out = []
    for m in moons:
        out.append((m.pos(), m.vel()))

    return out


def step(moons):
    for m1 in moons:
        for m2 in moons:
            m1.compare(m2.pos())

    for m in moons:
        m.update_velocity()
        m.move()


# moons = [Moon(-4, 3, 15), Moon(-11, -10, 13), Moon(2, 2, 18), Moon(7, -1, 0)]
x_moons = [Moon2(-4), Moon2(-11), Moon2(2), Moon2(7)]
y_moons = [Moon2(3), Moon2(-10), Moon2(2), Moon2(-1)]
z_moons = [Moon2(15), Moon2(13), Moon2(18), Moon2(0)]

i = 0
x_initial = state(x_moons)
y_initial = state(y_moons)
z_initial = state(z_moons)
x_val = 0
y_val = 0
z_val = 0
while i < 1000000 and (x_val == 0 or y_val == 0 or z_val == 0):
    i += 1

    if x_val == 0:
        step(x_moons)
        if x_initial == state(x_moons):
            x_val = i
            print('>>> ' + str(i))

    if y_val == 0:
        step(y_moons)
        if y_initial == state(y_moons):
            y_val = i
            print('>>> ' + str(i))

    if z_val == 0:
        step(z_moons)
        if z_initial == state(z_moons):
            z_val = i
            print('>>> ' + str(i))

print(x_val * y_val * z_val / (gcd(x_val, y_val) * gcd(x_val, z_val)))
