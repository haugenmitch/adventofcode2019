def compose(f, g):
    return (g[0] * f[0]) % num_cards, (g[0] * f[1] + g[1]) % num_cards


def pow_mod(x, n, m):
    y = 1
    while n > 0:
        if n % 2 == 1:
            y = (y * x) % m
        n = n // 2
        x = (x * x) % m
    return y


with open('input.txt') as file:
    cmds = file.readlines()

num_cards = 119315717514047
num_shuffles = 101741582076661
original_index = 2020

lcf = (1, 0)

for cmd in cmds:
    cmd = cmd.strip()

    if cmd.startswith('deal into'):
        lcf = compose(lcf, (-1, -1))
    elif cmd.startswith('cut'):
        n = int(cmd.split(' ')[-1])
        lcf = compose(lcf, (1, -n))
    elif cmd.startswith('deal with'):
        n = int(cmd.split(' ')[-1])
        lcf = compose(lcf, (n, 0))
    else:
        print('error: %s' % cmd)

answer = (1, 0)
iterations = num_shuffles
while iterations > 0:
    if iterations % 2 == 1:
        answer = compose(answer, lcf)
    iterations = iterations // 2
    lcf = compose(lcf, lcf)

print((original_index - answer[1]) * pow_mod(answer[0], num_cards - 2, num_cards) % num_cards)
