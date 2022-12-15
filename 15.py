from aocd import lines
from aocd import submit
import re

sensors = list(map(lambda e: list(map(int, re.findall(r'-?\d+', e))), lines))

def not_in_range(x, y):
    return all(map(lambda e:
        abs(x - e[0]) + abs(y - e[1]) > abs(e[2] - e[0]) + abs(e[3] - e[1]), sensors))

def get_invisible_pos(sx, sy, d, xy_checker):
    x = sx
    y = sy - d - 1
    for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
        for i in range(d):
            if xy_checker(x, y) and not_in_range(x, y):
                return x, y
            x += dx
            y += dy
    return None

row = 2000000
free_positions = set()

size = 4000000
invisible_pos = None

for sx, sy, bx, by in sensors:
    d = abs(bx - sx) + abs(by - sy)
    for dx in range(-d + abs(row - sy), d - abs(row - sy) + 1):
        x = sx + dx
        if row != by or x != bx:
            free_positions.add(x)

    if invisible_pos is None:
        invisible_pos = get_invisible_pos(sx, sy, d,
            lambda x, y: x >= 0 and x <= size and y >= 0 and y <= size)

submit(len(free_positions), part='a')
submit(invisible_pos[0] * size + invisible_pos[1], part='b')
