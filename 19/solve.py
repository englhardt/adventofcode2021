import itertools, parse

def transform(mes, ax, neg):
    return [(neg[0] * x[ax[0]], neg[1] * x[ax[1]], neg[2] * x[ax[2]]) for x in mes]

def shift(mes, s):
    return [(x[0] + s[0], x[1] + s[1], x[2] + s[2]) for x in mes]

def test(a, b_orig):
    a_set = set(a)
    for ax in options_axis:
        for neg in options_neg:
            b = transform(b_orig, ax, neg)
            for pa in a:
                for pb in b:
                    shift_val = (pa[0] - pb[0], pa[1] - pb[1], pa[2] - pb[2])
                    b_shifted = shift(b, shift_val)
                    matches = len(a_set.intersection(b_shifted))
                    if matches >= 12:
                        return True, shift_val, b_shifted
    return False, None, None

raw = open('input.txt').read().split('---')
sensors = [[x.fixed for x in parse.findall('{:d},{:d},{:d}\n', l)] for l in raw[2::2]]
options_axis = list(itertools.permutations([0, 1, 2]))
options_neg = [[a, b, c] for a in [-1, 1] for b in [-1, 1] for c in [-1, 1]]

shift_vals = {0: (0, 0, 0)}
aligned = {0: sensors[0]}
beacons = set(sensors[0])
noalign = set()
while len(shift_vals) < len(sensors):
    done = False
    for i in range(len(sensors)):
        if i not in shift_vals:
            for j, ss in list(shift_vals.items()):
                if (i, j) in noalign:
                    continue
                done, *d = test(aligned[j], sensors[i])
                if done:
                    shift_vals[i] = d[0]
                    aligned[i] = d[1]
                    beacons.update(aligned[i])
                    print(f'Aligned {i} to {j}. Shift: {d[0]}, Global pos: {shift_vals[i]}, |B| = {len(beacons)}')
                    break
                noalign.add((i, j))
        if done:
            break

print(len(beacons))
dists = []
for a in shift_vals.values():
    for b in shift_vals.values():
        dists.append(abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]))
print(max(dists))
