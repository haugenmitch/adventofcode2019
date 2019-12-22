import sys

with open(sys.argv[1]) as f:
    image = [int(d) for d in f.read().strip()]

layers = []
while len(image) > 0:
    layers.append([])
    for i in range(150):
        layers[-1].append(image.pop())

least = []
count = 150
for layer in layers:
    if layer.count(0) < count:
        count = layer.count(0)
        least = layer

print(least.count(1)*least.count(2))