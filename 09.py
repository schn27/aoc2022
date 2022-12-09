from aocd import lines
from aocd import submit

moves = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}

knots = [(0, 0) for _ in range(10)]

visited1, visited2 = set(), set()
visited1.add(knots[1])
visited2.add(knots[-1])

for line in lines:
    d, n = line.split()

    for i in range(int(n)):
        knots[0] = tuple(sum(x) for x in zip(knots[0], moves[d]))

        for i in range(1, len(knots)):
            diff = [h - t for h, t in zip(knots[i - 1], knots[i])]

            if abs(diff[0]) == 2 or abs(diff[1]) == 2:
                diff = map(lambda e: min(max(e, -1), 1), diff)
                knots[i] = tuple(sum(x) for x in zip(knots[i], diff))

        visited1.add(knots[1])
        visited2.add(knots[-1])

submit(len(visited1), part='a')
submit(len(visited2), part='b')
