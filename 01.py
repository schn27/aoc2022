from aocd import data
from aocd import submit

elves = map(lambda e: sum(map(int, e.split())), data.split('\n\n'))
elves = sorted(elves, reverse=True)

submit(elves[0], part='a')
submit(elves[0] + elves[1] + elves[2], part='b')
