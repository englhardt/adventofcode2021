commands = [(x[:-2], int(x[-1])) for x in open('input.txt').read().splitlines()]
x, y, z = 0, 0, 0
for c, i in commands:
    match c:
        case 'forward':
            x += i
            z += i * y
        case 'down':
            y += i
        case 'up':
            y -= i
print(x * y)
print(x * z)
