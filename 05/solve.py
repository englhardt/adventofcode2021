from collections import Counter

def calc_points(lines, p2=False):
    points_covered = []
    for l in lines:
        start, end = [list(map(int, p.split(','))) for p in l.split(' -> ')]
        if start[0] == end[0] or start[1] == end[1]:
            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    points_covered.append([i, j])
        elif p2 and abs(start[0] - end[0]) == abs(start[1] - end[1]):
            dx = -1 if start[0] > end[0] else 1
            dy = -1 if start[1] > end[1] else 1
            for i in range(abs(start[0] - end[0]) + 1):
                points_covered.append([start[0] + dx * i, start[1] + dy * i])
    counts = Counter([str(x) for x in points_covered])
    return len([x for x in counts.values() if x > 1])

lines = open('input.txt').read().splitlines()
print(calc_points(lines))
print(calc_points(lines, True))
