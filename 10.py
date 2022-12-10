from aocd import lines
from aocd import submit

x = 1
track = []

for line in lines:
    opcode, *arg = line.split()
    track.append(x)

    if opcode == 'addx':
        track.append(x)
        x += int(arg[0])

submit(sum(map(lambda t: t * track[t - 1], [20, 60, 100, 140, 180, 220])), part='a')

print('Part b (manual submit):')

row = []
for x in track:
    t = len(row) + 1
    row.append('#' if t >= x and t <= x + 2  else '.')
    if len(row) >= 40:
        print(''.join(row))
        row = []
