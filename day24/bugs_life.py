# ..##.
# ..#..
# ##...
# #....
# ...##

def state(rating, ind):
    neighbors = 0
    if ind > 4 and ((rating & (1 << (ind - 5))) > 0):
        neighbors += 1
    if rating & (1 << (ind + 5)):
        neighbors += 1
    if ind//5 == (ind+1)//5 and rating & (1 << (ind+1)):
        neighbors += 1
    if ind//5 == (ind-1)//5 and rating & (1 << (ind-1)):
        neighbors += 1
    if rating & (1 << ind):
        if neighbors == 1:
            return 1
        else:
            return 0
    else:
        if neighbors == 1 or neighbors == 2:
            return 1
        else:
            return 0


ratings = [0b1100000001000110010001100]

while True:
    prev = ratings[-1]
    next = 0
    for i in range(25):
        next += state(prev, i) << i

    if next in ratings:
        print(next)
        break

    ratings.append(next)
