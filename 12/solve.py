from collections import defaultdict, Counter
lines = open('input.txt').read().splitlines()
edges = defaultdict(list)
for l in lines:
    a, b = l.split('-')
    edges[a].append(b)
    edges[b].append(a)
big_caves = [e for e in edges if not e.islower()]
small_caves = [e for e in edges if e.islower() and e not in ['start', 'end']]

def find_paths(pos, path, p2=False):
    if pos == 'end':
        yield path
        return
    for e in edges[pos]:
        if not p2 and not (e not in big_caves and e in path):
            yield from find_paths(e, path + [e])
        elif p2:
            counts = Counter(path)
            if e != 'start' and (e in big_caves or e not in path or \
                                 not any(counts[e] > 1 for e in small_caves)):
                yield from find_paths(e, path + [e], p2)

print(len([x for x in find_paths('start', ['start'], False)]))
print(len([x for x in find_paths('start', ['start'], True)]))
