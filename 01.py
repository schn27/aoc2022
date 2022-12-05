from aocd import data
from aocd import submit

elves = list(map(lambda e: sum(map(int, e.split())), data.split('\n\n')))
elves.sort(reverse=True)

submit(elves[0], part='a')
submit(sum(elves[0:3]), part='b')
