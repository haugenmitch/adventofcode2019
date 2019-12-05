import re, sys

def isValid(n):
    digits = [int(x) for x in str(n)]

    repeat = False
    prev = 0
    for d in digits:
        if d < prev:
            return False
        if d == prev:
            repeat = True
        prev = d

    return repeat


minimum = int(sys.argv[1])
maximum = int(sys.argv[2])

count = 0
for i in range(minimum, maximum+1):
    if isValid(i):
        count = count + 1

print(count)
