from aocd import lines
from aocd import submit

cubes = dict(map(lambda e: (tuple(map(int, e.split(','))), 6), lines))

surface = 0

dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

for x, y, z in cubes:
    for dx, dy, dz in dirs:
        if (x + dx, y + dy, z + dz) in cubes:
            cubes[(x, y, z)] -= 1

    surface += cubes[(x, y, z)]

cube = sorted(iter(cubes), key=lambda e:e[0])[0]

wave = [(cube[0] - 1, cube[1], cube[2])]
water = set()
water.add(wave[0])

neighbors = [(dx, dy, dz) for dx in range(-1, 2) for dy in range(-1, 2) for dz in range(-1, 2)
    if dx != 0 or dy != 0  or dz != 0]

while len(wave) > 0:
    next_wave = set()

    for x, y, z in wave:
        candidates = map(lambda e: (x + e[0], y + e[1], z + e[2]), dirs)
        candidates = filter(lambda e: not (e in water or e in next_wave or e in cubes), candidates)
        candidates = filter(lambda e: any(map(lambda ee: (e[0] + ee[0], e[1] + ee[1], e[2] + ee[2]) in cubes, neighbors)), candidates)
        next_wave.update(candidates)

    wave = next_wave
    water.update(wave)

surface2 = 0

for x, y, z in cubes:
    surface2 += sum(map(lambda e: int((x + e[0], y + e[1], z + e[2]) in water), dirs))

submit(surface, part='a')
submit(surface2, part='b')
