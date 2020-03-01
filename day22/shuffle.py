from copy import deepcopy

with open('input.txt') as f:
    cmds = f.readlines()

deck = list(range(10007))

for cmd in cmds:
    cmd = cmd.strip()

    if cmd.startswith('deal into'):
        deck.reverse()
    elif cmd.startswith('cut'):
        n = int(cmd.split(' ')[-1])
        deck = deck[n:] + deck[0:n]
    elif cmd.startswith('deal with'):
        n = int(cmd.split(' ')[-1])
        temp = [0] * 10007
        for i, val in enumerate(deck):
            temp[(i * n) % 10007] = val
        deck = deepcopy(temp)
    else:
        print('error: %s' % cmd)

print(deck.index(2019))
