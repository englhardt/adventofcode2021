import parse

lines = open('input.txt').read()
dots = parse.findall('{:d},{:d}', lines)
folds = parse.findall('{:l}={:d}', lines)

for i, (axis, pos) in enumerate(folds):
    dots = {(min(2 * pos - x, x) if axis == 'x' else x,
             min(2 * pos - y, y) if axis == 'y' else y)
             for x, y in dots}
    if i == 0:
        print(len(dots))

for y in range(6):
    print(''.join(' ' if (x, y) not in dots else '#' for x in range(40)))
