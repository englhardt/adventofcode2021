def find_neighbors(x, y):
    pos = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if x + dx >= 0 and x + dx < GRID_SIZE \
                and y + dy >= 0 and y + dy < GRID_SIZE \
                and not (dx == 0 and dy == 0):
                pos.append((x + dx, y + dy))
    return pos

def flash(pos, grid, flashed):
    grid[pos] = 0
    flashed.add(pos)
    to_flash = set()
    for n in find_neighbors(pos[0], pos[1]):
        if n not in flashed:
            grid[n] += 1
            if grid[n] > 9:
                to_flash.add(n)
    for n in to_flash:
        if n not in flashed:
            flash(n, grid, flashed)

lines = open('input.txt').read().splitlines()
GRID_SIZE = len(lines)
grid = {(x, y): int(v) for y, l in enumerate(lines) for x, v in enumerate(l)}
flash_count = 0
for i in range(10000):
    flashed = set()
    for pos in grid:
        grid[pos] += 1
    for pos in grid:
        if grid[pos] > 9:
            flash(pos, grid, flashed)
    flash_count += len(flashed)
    if i == 99:
        print(flash_count)
    if len(flashed) == 10 * 10:
        print(i + 1)
        break
