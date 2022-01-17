from collections import Counter

l = open('input.txt').read().splitlines()
g = ''.join([max(set(x), key=x.count) for x in zip(*l)])
print(int(g, 2) * (int(g, 2) ^ 0xFFF))

rest_oxy = l[:]
rest_co2 = l[:]
for i in range(len(l[0])):
    counts = Counter(x[i] for x in rest_oxy)
    mcv, mcc = counts.most_common()[0]
    rest_oxy = [x for x in rest_oxy if x[i] == (mcv if mcc != len(rest_oxy) / 2 else '1')]
    counts = Counter(x[i] for x in rest_co2)
    lcv, lcc = counts.most_common()[:-len(rest_co2)-1:-1][0]
    rest_co2 = [x for x in rest_co2 if x[i] == (lcv if lcc != len(rest_co2) / 2 else '0')]
print(int(rest_oxy[0], 2) * int(rest_co2[0], 2))
