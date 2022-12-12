from aocd import lines
from aocd import submit

def get_height(c):
    return 'abcdefghijklmnopqrstuvwxyz'.index('a' if c == 'S' else 'z' if c == 'E' else c)

heightmap = []
start = None
end = None

for y, line in enumerate(lines):
    start = start if not 'S' in line else (line.index('S'), y)
    end = end if not 'E' in line else (line.index('E'), y)
    heightmap.append([get_height(c) for c in line])

steps = {end: 0}
wave = set()
wave.add(end)

max_x, max_y = len(heightmap[0]), len(heightmap)

while len(wave) > 0:
    next_wave = set()

    for x, y in wave:
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            xx = x + dx
            yy = y + dy
            inside = xx >= 0 and xx < max_x and yy >= 0 and yy < max_y

            if inside and not (xx, yy) in steps and heightmap[y][x] - heightmap[yy][xx] <= 1:
                steps[(xx, yy)] = steps[(x, y)] + 1
                next_wave.add((xx, yy))

    wave = next_wave

submit(steps[start], part='a')

steps_from_a = []

for y, row in enumerate(heightmap):
    for x, c in enumerate(row):
        if c == 0 and (x, y) in steps:
            steps_from_a.append(steps[(x, y)])

submit(min(steps_from_a), part='b')
