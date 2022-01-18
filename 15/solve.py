import networkx as nx

def find_neighbors(x, y):
    for xx, yy in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
        if xx >= 0 and xx < GRID_SIZE and yy >= 0 and yy < GRID_SIZE:
            yield (xx, yy)

def solve(grid):
    g = nx.DiGraph()
    for (x, y), v in grid.items():
        g.add_weighted_edges_from([((x, y), n, grid[n]) for n in find_neighbors(x, y)])
    return nx.dijkstra_path_length(g, (0, 0), (GRID_SIZE - 1, GRID_SIZE - 1))

lines = [[int(x) for x in l] for l in open('input.txt').read().splitlines()]
grid = {(x, y): int(v) for y, l in enumerate(lines) for x, v in enumerate(l)}
GRID_SIZE = len(lines)
print(solve(grid))

for (x, y), v in list(grid.items()):
    for i in range(5):
        for j in range(5):
            val = i + j + v
            grid[x + i * GRID_SIZE, y + j * GRID_SIZE] = val if val < 10 else val - 9
GRID_SIZE = GRID_SIZE * 5
print(solve(grid))
