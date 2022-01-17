lines = open('input.txt').read().splitlines()
c = 0
for l in lines:
    digits = [len(x) for x in l.split(' | ')[1].split()]
    for d in digits:
        if d in [2, 3, 4, 7]:
            c += 1
print(c)

def decode(l):
    coded = [set(c) for c in l.split(' | ')[0].split()]
    coded_with_len = {len(x): x for x in coded}
    lookup = {1: coded_with_len[2],
              4: coded_with_len[4],
              7: coded_with_len[3],
              8: coded_with_len[7]}
    for c in coded:
        if c not in lookup.values():
            if len(c) == 5:
                if lookup[7] < c:
                    lookup[3] = c
                elif len(lookup[4].intersection(c)) == 3:
                    lookup[5] = c
                else:
                    lookup[2] = c
            else:
                if lookup[4] < c:
                    lookup[9] = c
                elif lookup[7] < c:
                    lookup[0] = c
                else:
                    lookup[6] = c
    reverse_lookup = {''.join(sorted(v)): str(k) for k, v in lookup.items()}
    output = [''.join(sorted(x)) for x in l.split(' | ')[1].split()]
    return int(''.join([reverse_lookup[x] for x in output]))

print(sum(map(decode, lines)))
