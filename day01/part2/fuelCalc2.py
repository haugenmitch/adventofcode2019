import sys

def calcFuel(mass):
    if mass < 9:
        return 0

    fuel = mass//3 - 2
    return fuel + calcFuel(fuel)

with open(sys.argv[1]) as f:
    nums = [int(x) for x in f]

total = 0
for n in nums:
    total += calcFuel(n)

print(total)
