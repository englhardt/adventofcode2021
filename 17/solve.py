import parse

raw = open('input.txt').read().rstrip()
(x_min, x_max), (y_min, y_max) = [x for x in parse.findall('={:d}..{:d}', raw)]

hit = lambda x, y: x_min <= x <= x_max and y_min <= y <= y_max
overshot = lambda x, y: x > x_max or y < y_min

def shoot(vx, vy):
    x, y = 0, 0
    max_y = -100000
    while not overshot(x, y):
        x, y = x + vx, y + vy
        vx = vx - 1 if vx > 0 else min(0, vx + 1)
        vy -= 1
        max_y = max(y, max_y)
        if hit(x, y):
            return max_y, True
    return max_y, False

best_height = -1000000
hits = 0
for vx in range(2 * x_max):
    for vy in range(-2 * abs(y_min), 2 * abs(y_min)):
        max_y, did_hit = shoot(vx, vy)
        hits += did_hit
        if did_hit and max_y > best_height:
            best_height = max_y
print(best_height)
print(hits)
