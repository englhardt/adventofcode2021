import math

def parse(d):
    global sum_v
    v, t = int(d[:3], 2), int(d[3:6], 2)
    d = d[6:]
    sum_v += v
    if t == 4:
        literal = ''
        while d[0] == '1':
            literal += d[1:5]
            d = d[5:]
        literal += d[1:5]
        d = d[5:]
        return d, (v, t, int(literal, 2))
    else:
        sub_packets = []
        if d[0] == '0':
            sub_len = int(d[1:16], 2)
            d = d[16:]
            d_sub = d[:sub_len]
            while d_sub:
                d_sub, pkg = parse(d_sub)
                sub_packets.append(pkg)
            d = d[sub_len:]
        else:
            num_sub = int(d[1:12], 2)
            d = d[12:]
            for _ in range(num_sub):
                d, pkg = parse(d)
                sub_packets.append(pkg)
        return d, (v, t, sub_packets)

def solve(p):
    match p[1]:
        case 0:
            return sum(solve(x) for x in p[2])
        case 1:
            return math.prod(solve(x) for x in p[2])
        case 2:
            return min(solve(x) for x in p[2])
        case 3:
            return max(solve(x) for x in p[2])
        case 4:
            return p[2]
        case 5:
            return int(solve(p[2][0]) > solve(p[2][1]))
        case 6:
            return int(solve(p[2][0]) < solve(p[2][1]))
        case 7:
            return int(solve(p[2][0]) == solve(p[2][1]))

raw = open('input.txt').read().rstrip()
d = ''.join([f'{int(x, 16):0>4b}' for x in raw])
sum_v = 0
parsed = parse(d)[1]
print(sum_v)
print(solve(parsed))
