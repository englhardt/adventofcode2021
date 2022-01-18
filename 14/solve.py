import parse
from collections import Counter, defaultdict

lines = open('input.txt').read()
start = lines.splitlines()[0]
rules = {k: v for k, v in parse.findall('{:l} -> {:l}', lines)}
pairs = [a + b for a, b in zip(start, start[1:])]
counts = Counter(pairs)
char_counts = Counter(start)

for i in range(40):
    for (a, b), v in counts.copy().items():
        if v > 0 and (ins := rules.get(a + b)):
            counts[a + ins] += v
            counts[ins + b] += v
            counts[a + b] -= v
            char_counts[ins] += v
    if i == 9 or i == 39:
        print(max(char_counts.values()) - min(char_counts.values()))
