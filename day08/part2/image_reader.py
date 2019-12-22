import sys

with open(sys.argv[1]) as f:
    image = [int(d) for d in f.read().strip()]

layers = []
while len(image) > 0:
    layers.append([])
    for i in range(150):
        layers[-1].append(image.pop(0))

base = layers[0]

for i, n in enumerate(base):
    if n == 2:
        for layer in layers:
            if layer[i] != 2:
                base[i] = layer[i]
                break

base = ['#' if x == 1 else ' ' for x in base]

print(''.join(base[0:25]))
print(''.join(base[25:50]))
print(''.join(base[50:75]))
print(''.join(base[75:100]))
print(''.join(base[100:125]))
print(''.join(base[125:]))