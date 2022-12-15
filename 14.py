from aocd import lines
from aocd import submit
import re

walls = map(lambda e: map(int, re.findall(r'\d+', e)), lines)

world = set()
max_y = 0

for wall in walls:
    wall = list(zip(* [iter(wall)] * 2))
    for i in range(1, len(wall)):
        x, y = wall[i - 1]
        x1, y1 = wall[i]
        dx = min(max(x1 - x, -1), 1)
        dy = min(max(y1 - y, -1), 1)
        while y != y1 + dy or x != x1 + dx:
            max_y = max(max_y, y)
            world.add((x, y))
            x += dx
            y += dy

start_x, start_y = 500, 0
x, y = start_x, start_y
cnt_a = None
cnt_b = 0

branches = []

while not (start_x, start_y) in world:
    left, down, right = (x - 1, y + 1) in world, (x, y + 1) in world, (x + 1, y + 1) in world
    if (left and down and right) or (y + 1 == max_y + 2):
        world.add((x, y))
        cnt_b += 1
        x, y = start_x, start_y
        x, y = branches.pop() if len(branches) else (start_x, start_y)
    else:
        if down:
            branches.append((x, y))
            x += 1 if left else -1
        y += 1

    if y >= max_y and cnt_a is None:
        cnt_a = cnt_b

submit(cnt_a, part='a')
submit(cnt_b, part='b')
