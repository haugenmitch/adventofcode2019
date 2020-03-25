def step(level_0, level_1, level_2):
    new_level = 0

    for i in range(25):
        new_level <<= 1

        if i == 12:
            continue

        neighbors = 0

        # top
        if i < 5:
            neighbors += level_2 >> 7 & 1
        elif i == 17:
            top_edge = level_0 & (0b11111 << 20)
            while top_edge != 0:
                neighbors += top_edge & 1
                top_edge >>= 1
        else:
            neighbors += level_1 >> (i - 5) & 1

        # bottom
        if i >= 20:
            neighbors += level_2 >> 17 & 1
        elif i == 7:
            bottom_edge = level_0 & 0b11111
            while bottom_edge != 0:
                neighbors += bottom_edge & 1
                bottom_edge >>= 1
        else:
            neighbors += level_1 >> (i + 5) & 1

        # left
        if i % 5 == 0:
            neighbors += level_2 >> 11 & 1
        elif i == 13:
            left_edge = level_0 & 0b1000010000100001000010000
            while left_edge != 0:
                neighbors += left_edge & 1
                left_edge >>= 1
        else:
            neighbors += level_1 >> (i - 1) & 1

        # right
        if i % 5 == 4:
            neighbors += level_2 >> 13 & 1
        elif i == 11:
            right_edge = level_0 & 0b0000100001000010000100001
            while right_edge != 0:
                neighbors += right_edge & 1
                right_edge >>= 1
        else:
            neighbors += level_1 >> (i + 1) & 1

        alive = level_1 >> i & 1
        if (alive and neighbors == 1) or (not alive and (neighbors == 1 or neighbors == 2)):
            new_level += 1

    return new_level


levels = [0, 0b1100000001000110010001100, 0]

for i in range(200):
    new_levels = []
    for j in range(len(levels)):
        if j == 0:
            lvl_0 = 0
        else:
            lvl_0 = levels[j - 1]

        if j+1 == len(levels):
            lvl_2 = 0
        else:
            lvl_2 = levels[j + 1]

        new_levels.append(step(lvl_0, levels[j], lvl_2))

    levels = new_levels

    if levels[0] != 0:
        levels.insert(0, 0)
    if levels[-1] != 0:
        levels.append(0)

total_bugs = 0

for level in levels:
    while level != 0:
        total_bugs += level & 1
        level >>= 1

print(total_bugs)
