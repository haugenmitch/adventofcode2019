from moon import Moon

moons = [Moon(-4, 3, 15), Moon(-11, -10, 13), Moon(2, 2, 18), Moon(7, -1, 0)]

for i in range(1000):
    for moon1 in moons:
        for moon2 in moons:
            moon1.compare(moon2.pos())

    for moon in moons:
        moon.update_velocity()
        moon.move()

total = 0
for moon in moons:
    total += moon.energy()

print(total)