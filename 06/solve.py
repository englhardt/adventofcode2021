d = list(map(int, open('input.txt').read().split(',')))
counts = {i: d.count(i) for i in range(9)}
for i in range(256):
    counts = {0: counts[1], 1: counts[2], 2: counts[3], 3: counts[4], 4: counts[5],
              5: counts[6], 6: counts[7] + counts[0], 7: counts[8], 8: counts[0]}
    if i == 79:
        print(sum(counts.values()))
print(sum(counts.values()))
