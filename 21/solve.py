raw = [int(x[-1]) - 1 for x in open('input.txt').read().splitlines()]
d = raw[:]
score = [0, 0]
rolls, won = 0, False
while not won:
    for i in range(2):
        val = 3 * (rolls + 1) + 3
        rolls += 3
        d[i] = (d[i] + val) % 10
        score[i] += d[i] + 1
        if score[i] >= 1000:
            won = True
            break
print(rolls * min(score))

def sim(p1, p2, s1, s2):
    if s1 >= 21 or s2 >= 21:
        return (s1 >= 21, s2  >= 21)
    if (p1, p2, s1, s2) in STATES:
        return STATES[(p1, p2, s1, s2)]
    w1, w2 = 0, 0
    for r1 in rolls:
        new_p1 = (p1 + r1) % 10
        new_s1 = s1 + new_p1 + 1
        new_w2, new_w1 = sim(p2, new_p1, s2, new_s1)
        w1, w2 = w1 + new_w1, w2 + new_w2
    STATES[(p1, p2, s1, s2)] = (w1, w2)
    return w1, w2

rolls = [sum([x, y, z]) for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]]
STATES = {}
print(max(sim(raw[0], raw[1], 0, 0)))
