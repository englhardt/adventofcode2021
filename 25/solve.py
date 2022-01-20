import copy

grid = [list(x) for x in open('input.txt').read().splitlines()]
N, M = len(grid[0]), len(grid)
i, moved = 0, True
while moved:
    moved = False
    new_grid = copy.deepcopy(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == '>' and grid[y][(x + 1) % N] == '.':
                new_grid[y][x] = '.'
                new_grid[y][(x + 1) % N] = '>'
                moved = True
    grid = new_grid
    new_grid = copy.deepcopy(grid)
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 'v' and grid[(y + 1) % M][x] == '.':
                new_grid[y][x] = '.'
                new_grid[(y + 1) % M][x] = 'v'
                moved = True
    grid = new_grid
    i += 1
print(i)
