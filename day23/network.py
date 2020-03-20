from computer import Computer

nics = []
for i in range(50):
    nics.append(Computer('input.txt'))
    nics[i].input(i)
    nics[i].run()

print('start')

while True:
    for i in range(50):
        if nics[i].input_requested():
            nics[i].input(-1)
        if nics[i].output_ready():
            out = nics[i].output()
            print(out)
            while len(out):
                dest = out.pop(0)
                x = out.pop(0)
                y = out.pop(0)
                if dest == 255:
                    print(y)
                    break
                nics[dest].input([x, y])
        nics[i].run()

print('done')
