l = open('input.txt').read().splitlines()
draw = list(map(int, l[0].split(',')))
boards = []
for i in range((len(l) - 1) // 6):
    b = []
    for j in range(5):
        b.append(list(map(int, l[i * 6 + j + 2].split())))
    boards.append(b)

# transform to sets
board_sets = []
for b in boards:
    cur_sets = [set(r) for r in b]
    cur_sets += [set(c) for c in zip(*b)]
    board_sets.append(cur_sets)

won = [False] * len(boards)
i = 5
while not all(won):
    win_con = set(draw[:i])
    for bid, b in enumerate(board_sets):
        if not won[bid] and any(x <= win_con for x in b):
            win_score = sum(set.union(*b) - win_con) * draw[i - 1]
            if not any(won):
                print(win_score)
            won[bid] = win_score
        if all(won):
            print(won[bid])
            break
    i += 1
