from computer import Computer

nics = []
for i in range(50):
    nics.append(Computer('input.txt'))
    nics[i].input(i)
    nics[i].run()

print('start')

nat_x = -1
nat_y = -1
last_y = -1
while True:
    idle = True
    for i in range(50):
        nics[i].run()
        if nics[i].input_requested():
            nics[i].input(-1)
        if nics[i].output_ready():
            idle = False
            out = nics[i].output()
            print(out)
            while len(out):
                dest = out.pop(0)
                x = out.pop(0)
                y = out.pop(0)
                if dest == 255:
                    nat_x = x
                    nat_y = y
                else:
                    nics[dest].input([x, y])

    if idle:
        if nat_y == last_y:
            print(nat_y)
            break
        last_y = nat_y
        nics[0].input([nat_x, nat_y])

print('done')
