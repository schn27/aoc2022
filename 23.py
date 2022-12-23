from aocd import lines
from aocd import submit

NW, N, NE, W, E, SW, S, SE = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
dirs = (NW, N, NE, W, E, SW, S, SE)
moves = (((N, NE, NW), N), ((S, SE, SW), S), ((W, NW, SW), W), ((E, NE, SE), E))

def check(elf, dirs, elves):
    return map(lambda e: not ((elf[0] + e[0], elf[1] + e[1]) in elves), dirs)

def get_empty_tiles(elves):
    xx, yy = zip(*elves)
    minx, maxx = min(xx), max(xx)
    miny, maxy = min(yy), max(yy)
    return (maxx - minx + 1) * (maxy - miny + 1) - len(elves)

elves = [(x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '#']

round_number = 1
while True:
    elves_set = set(elves)
    new_elves = []
    collisions = {}
    count_fixed = 0

    for elf in elves:
        new_elf = elf

        if not all(check(elf, dirs, elves_set)):
            for i in range(len(moves)):
                neigbours, move = moves[(i + round_number - 1) % len(moves)]
                if all(check(elf, neigbours, elves_set)):
                    new_elf = (elf[0] + move[0], elf[1] + move[1])
                    break
        else:
            count_fixed += 1

        new_elves.append(new_elf)

        if new_elf in collisions:
            collisions[new_elf] += 1
        else:
            collisions[new_elf] = 0

    elves = list(map(lambda e: e[1] if collisions[e[1]] == 0 else e[0], zip(elves, new_elves)))

    if round_number == 10:
        submit(get_empty_tiles(elves), part='a')

    if count_fixed == len(elves):
        submit(round_number, part='b')
        break

    round_number += 1
