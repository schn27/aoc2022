from aocd import lines
from aocd import submit

def get_visibility_and_count(line):
    for i, e in enumerate(line[1:]):
        if e >= line[0]:
            return (False, i + 1)

    return (True, len(line) - 1)

trees = list(map(lambda e: list(map(int, e)), lines))

visible = 0
max_score = 0

for r, row in enumerate(trees):
    for c, _ in enumerate(row):
        col = list(map(lambda e: e[c], trees))
        dirs = [list(reversed(row[:c + 1])), row[c:], list(reversed(col[:r + 1])), col[r:]]
        visibility, count = list(zip(*map(get_visibility_and_count, dirs)))
        visible += int(any(visibility))
        max_score = max(max_score, count[0] * count[1] * count[2] * count[3])

submit(visible, part='a')
submit(max_score, part='b')
