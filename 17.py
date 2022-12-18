from aocd import data
from aocd import submit
from itertools import cycle

figures = [
    [0b00111100],
    [0b00010000, 0b00111000, 0b00010000],
    [0b00111000, 0b00001000, 0b00001000],
    [0b00100000, 0b00100000, 0b00100000, 0b00100000],
    [0b00110000, 0b00110000]
]

figure_iter = cycle(figures)
jet_iter = cycle(data)

chamber = [0b111111111]

def is_overlapped(figure, pos, chamber):
    return any(map(lambda e: e[0] & e[1] != 0, zip(figure, chamber[pos: pos + len(figure)])))

results = []

for rock in range(max(2022, len(figures) * len(data))):
    figure = next(figure_iter)

    position = len(chamber) + 3

    for j in range(len(figure) + 3):
        chamber.append(0b100000001)

    stop = False

    while not stop:
        jet = next(jet_iter)
        moved = list(map(lambda e: e << 1 if jet== '<' else e >> 1, figure))
        figure = figure if is_overlapped(moved, position, chamber) else moved

        if not is_overlapped(figure, position - 1, chamber):
            position -= 1
        else:
            for i, row in enumerate(figure):
                chamber[position + i] |= row
            stop = True

    while chamber[-1] == 0b100000001:
        chamber.pop()

    results.append(len(chamber) - 1)

submit(results[2022 - 1], part='a')

for period in range(1, len(results) // 3):
    if len({results[i + period] - results[i] for i in range(period, len(results) - period, period)}) <= 1:
        break

trillion = 1000000000000
d = trillion // period
r = trillion % period

part2 = results[period - 1] + (results[2 * period] - results[period]) * (d - 1) + (results[period + r] - results[period])

submit(part2, part='b')
