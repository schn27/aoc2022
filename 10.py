from aocd import lines
from aocd import submit
from advent_of_code_ocr import convert_array_6

x = 1
track = []

for line in lines:
    opcode, *arg = line.split()
    track.append(x)

    if opcode == 'addx':
        track.append(x)
        x += int(arg[0])

submit(sum(map(lambda t: t * track[t - 1], [20, 60, 100, 140, 180, 220])), part='a')

rows = []
row = []
for x in track:
    t = len(row) + 1
    row.append(int(t >= x and t <= x + 2))
    if len(row) == 40:
        rows.append(row)
        row = []

submit(convert_array_6(rows, fill_pixel=1, empty_pixel=0), part='b')
