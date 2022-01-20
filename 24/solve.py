# Solution: Manual analysis or encoding into a solver like Z3
# Source: https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpuxf5l/
# Explanation: https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hpuu3e0/

def run(inp, ins):
    stack = []
    for i in range(14):
        div, check, add = [int(ins[i * 18 + x][-1]) for x in [4, 5, 15]]
        if div == 1:
            stack.append((i, add))
        elif div == 26:
            j, add = stack.pop()
            inp[i] = inp[j] + add + check
            if inp[i] > 9:
                inp[j] -= inp[i] - 9
                inp[i] = 9
            if inp[i] < 1:
                inp[j] += 1 - inp[i]
                inp[i] = 1
    return ''.join(str(x) for x in inp)


ins = [x.split() for x in open('input.txt').read().splitlines()]
print(run([9] * 14, ins))
print(run([1] * 14, ins))
