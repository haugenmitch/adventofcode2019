import sys

with open(sys.argv[1]) as f:
    nums = [int(x) for x in f]

total = 0
for n in nums:
    total += n//3 - 2

print(total)
