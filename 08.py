from aocd import lines
from aocd import submit

trees = list(map(lambda e: list(map(int, e)), lines))

visible = 0
max_score = 0

for r in range(len(trees)):
    for c in range(len(trees[0])):
        is_visible = False

        cc = c - 1
        left = 0
        while (cc >= 0 and trees[r][c] > trees[r][cc]):
            cc -= 1
            left += 1

        from_left = cc < 0
        left += int(not from_left)

        cc = c + 1
        right = 0
        while (cc < len(trees[0]) and trees[r][c] > trees[r][cc]):
            cc += 1
            right += 1

        from_right = cc >= len(trees[0])
        right += int(not from_right)

        rr = r - 1
        up = 0
        while (rr >= 0 and trees[r][c] > trees[rr][c]):
            rr -= 1
            up += 1

        from_up = rr < 0
        up += int(not from_up)

        rr = r + 1
        down = 0
        while (rr < len(trees) and trees[r][c] > trees[rr][c]):
            rr += 1
            down += 1

        from_down = rr >= len(trees)
        down += int(not from_down)

        visible += int(from_left or from_right or from_up or from_down)
        max_score = max(max_score, left * right * up * down)

submit(visible, part='a')
submit(max_score, part='b')
