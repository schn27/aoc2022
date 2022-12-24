from aocd import lines
from aocd import submit

WIDTH = len(lines[0]) - 2
HEIGHT = len(lines) - 2
LURDC = ((-1, 0), (0, -1), (1, 0), (0, 1), (0, 0))

start_pos = (lines[0].index('.') - 1, -1)
finish_pos = (lines[-1].index('.') - 1, len(lines) - 2)

blizzards = []

for y, line in enumerate(lines[1:-1]):
    for x, c in enumerate(line[1:-1]):
        if c != '.':
            blizzards.append((x, y, c))

def get_blizzards_for_time(time):
    delta = {'<': LURDC[0], '^': LURDC[1], '>': LURDC[2], 'v': LURDC[3]}

    def move(blizzard):
        x, y, c = blizzard
        dx, dy = delta[c]
        x += dx * time
        y += dy * time
        x %= WIDTH
        y %= HEIGHT
        return (x, y)

    return set(map(move, blizzards))

def get_path(start, finish, t=0):
    xys = set([start])

    while not finish in xys:
        next_xys = set()
        next_blizzards = get_blizzards_for_time(t + 1)

        for xy in xys:
            def is_good_pos(xy):
                not_wall = xy[0] >= 0 and xy[0] < WIDTH and xy[1] >= 0 and xy[1] < HEIGHT
                not_blizzard = not (xy in next_blizzards)
                return xy == start or xy == finish or (not_wall and not_blizzard)

            next_xys.update(filter(is_good_pos, map(lambda e: (xy[0] + e[0], xy[1] + e[1]), LURDC)))

        t += 1
        xys = next_xys

    return t


t1 = get_path(start_pos, finish_pos)
t2 = get_path(start_pos, finish_pos, get_path(finish_pos, start_pos, t1))

submit(t1, part='a')
submit(t2, part='b')
