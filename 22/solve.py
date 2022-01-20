import parse

def size(cube):
    (x1, x2), (y1, y2), (z1, z2) = cube
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

def intersection(cube1, cube2):
    inters = tuple((max(cube1[i][0], cube2[i][0]), min(cube1[i][1], cube2[i][1])) for i in range(3))
    if any(inters[i][0] > inters[i][1] for i in range(3)):
        return None
    return inters

def calc_size(cube, others):
    num_on = size(cube)
    if not others:
        return num_on
    reduced_cubes = []
    for val, *o in others:
        inters = intersection(cube, o)
        if inters:
            reduced_cubes.append((val, *inters))
    for i, (val, *r) in enumerate(reduced_cubes):
        num_on -= calc_size(r, reduced_cubes[i+1:])
    return num_on

raw = open('input.txt').read().splitlines()
cubes = [[x[:2] == 'on'] + list(parse.findall('{:d}..{:d}', x)) for x in raw]
filtered_cubes = [[val, intersection(c, ((-50, 50), (-50, 50), (-50, 50)))] for val, *c in cubes]
filtered_cubes = [[val, *c] for val, c in filtered_cubes if c]
print(sum(calc_size(c, cubes[i+1:]) for i, (val1, *c) in enumerate(filtered_cubes) if val1))
print(sum(calc_size(c, cubes[i+1:]) for i, (val1, *c) in enumerate(cubes) if val1))
