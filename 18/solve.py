import copy, math

def parse(data, level):
    for x in data:
        if isinstance(x, list):
            yield from parse(x, level + 1)
        else:
            yield [x, level]

def add_left(d, i, val):
    if i == 0:
        return False
    else:
        d[i - 1][0] += val
        return True

def add_right(d, i, val):
    if i == len(d) - 1:
        return False
    else:
        d[i + 1][0] += val
        return True

def explode(d, i):
    a, b = d[i][0], d[i + 1][0]
    ladd = add_left(d, i, a)
    radd = add_right(d, i + 1, b)
    if ladd and radd:
        del d[i]
        d[i] = [0, 3]
    elif ladd:
        d[i + 1][0], d[i + 1][1] = 0, d[i + 1][1] - 1
        del d[i]
    elif radd:
        d[i][0], d[i][1] = 0, d[i][1] - 1
        del d[i + 1]
    return ladd or radd

def split(d, i):
    a, b = math.floor(d[i][0] / 2), math.ceil(d[i][0] / 2)
    d[i] = [a, d[i][1] + 1]
    d.insert(i + 1, [b, d[i][1]])

def add_level(d):
    for x in d:
        x[1] += 1
    return d

def add(a, b):
    return add_level(a) + add_level(b)

def sim(d):
    unstable = True
    while unstable:
        unstable = False
        for i in range(len(d) - 1):
            if d[i][1] >= 4 and d[i+1][1] == d[i][1]:
                unstable = explode(d, i)
                if unstable:
                    break
        if not unstable:
            for i in range(len(d)):
                if d[i][0] >= 10:
                    split(d, i)
                    unstable = True
                    break
    return d

def magnitude_lvl(d, level):
    if len(d) == 1:
        return d[0][0]
    i, val = 0, 0
    while i < len(d) - 1:
        if d[i][1] == level:
            d[i] = [3 * d[i][0] + 2 * d[i + 1][0], d[i][1] - 1]
            del d[i + 1]
        i += 1
    return val

def magnitude(d):
    for l in [3, 2, 1, 0]:
        magnitude_lvl(d, l)
    return d[0][0]

fish = [list(parse(eval(r), 0)) for r in open('input.txt').read().splitlines()]
d = copy.deepcopy(fish)
a = d[0]
for i in range(1, len(d)):
    a = add(a, d[i])
    a = sim(a)
print(magnitude(a))
print(max([magnitude(sim(add(copy.deepcopy(a), copy.deepcopy(b)))) for a in fish for b in fish if a != b]))
