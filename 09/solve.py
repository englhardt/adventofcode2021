import math

def loc_to_check(x, y):
    pos = []
    if x > 0:
        pos.append((x - 1, y))
    if x < 99:
        pos.append((x + 1, y))
    if y > 0:
        pos.append((x, y - 1))
    if y < 99:
        pos.append((x, y + 1))
    return pos

lines = [[int(x) for x in l] for l in open('input.txt').read().splitlines()]
lp = []
rl = 0
for x in range(len(lines[0])):
    for y in range(len(lines)):
        val = lines[y][x]
        if all(lines[oy][ox] > val for ox, oy in loc_to_check(x, y)):
            rl += 1 + val
            lp.append((x, y))
print(rl)

def expand_basin(p, visited):
    visited.add(p)
    for other in loc_to_check(p[0], p[1]):
        if other not in visited and lines[other[1]][other[0]] < 9:
            visited.add(other)
            expand_basin(other, visited)
    return visited

print(math.prod(sorted([len(expand_basin(p, set())) for p in lp])[-3:]))
