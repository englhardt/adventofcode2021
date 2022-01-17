lines = open('input.txt').read().splitlines()

matches = {'(': ')', '[': ']', '{': '}', '<': '>'}
penalty = {')': 3, ']': 57, '}': 1197, '>': 25137}
costs = {')': 1, ']': 2, '}': 3, '>': 4}

errors = []
incpl_costs = []
for i, l in enumerate(lines):
    expected_closings = []
    for c in l:
        if c in matches.keys():
            expected_closings.append(matches[c])
        else:
            if expected_closings[-1] != c:
                # corrupted
                errors.append((i, c))
                break
            else:
                del expected_closings[-1]
    if not errors or errors[-1][0] != i:
        # incomplete
        cur_costs = 0
        for c in expected_closings[::-1]:
            cur_costs = cur_costs * 5 + costs[c]
        incpl_costs.append(cur_costs)

print(sum(penalty[c] for _, c in errors))
print(sorted(incpl_costs)[len(incpl_costs) // 2])
