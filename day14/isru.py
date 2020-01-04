import sys
from math import ceil


def requirements(name, amount):
    multiplier = ceil(amount / quantities[name])
    leftover = multiplier * quantities[name] - amount
    if leftover != 0:
        if name in leftovers:
            leftovers[name] += leftover
        else:
            leftovers[name] = leftover
    temp = inputs[name]
    out = []
    for t in temp:
        out.append((t[0], t[1] * multiplier))
    return out


with open(sys.argv[1]) as f:
    lines = [line.strip().split('=>') for line in f.readlines()]

quantities = {}
inputs = {}
leftovers = {}
for line in lines:
    product = list(reversed(line[1].strip().split(' ')))
    chemicals = line[0].strip().split(', ')
    reactants = []
    for chemical in chemicals:
        parts = chemical.split(' ')
        reactants.append((parts[1], int(parts[0])))

    quantities[product[0]] = int(product[1])
    inputs[product[0]] = reactants

products = [('FUEL', 2074843)]
ore_requirement = 0
while len(products):
    product = products.pop(0)
    chem = product[0]
    n = product[1]
    if chem == 'ORE':
        ore_requirement += n
    else:
        if chem in leftovers and leftovers[chem] != 0:
            extra = min(n, leftovers[chem])
            leftovers[chem] -= extra
            n -= extra
        if n != 0:
            products = products + requirements(chem, n)

print(ore_requirement)