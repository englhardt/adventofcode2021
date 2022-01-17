d = list(map(int, open('input.txt').read().splitlines()))
print(sum(x < y for x, y in zip(d, d[1:])))
print(sum(x < y for x, y in zip(d, d[3:])))
