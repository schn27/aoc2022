from aocd import lines
from aocd import submit
import re
import copy

empty = lines.index('')

nstacks = int(re.findall(r'\d+', lines[empty - 1])[-1])
stacks = [[] for _ in range(nstacks)]

for line in lines[:empty - 1]:
    for i in range(nstacks):
        c = line[i * 4 + 1]
        if c.isalpha():
            stacks[i].append(c)

procedure = list(map(lambda e: list(map(int, re.findall(r'\d+', e))), lines[empty + 1:]))

def get_top_after_procedure(stacks, procedure, *, move_by_one):
    stacks = copy.deepcopy(stacks)

    for n, src, dst in procedure:
        p = stacks[src - 1][:n]
        stacks[src - 1] = stacks[src - 1][n:]
        if move_by_one:
            p.reverse()
        stacks[dst - 1] = p + stacks[dst - 1]

    return ''.join(map(lambda e: e[0], stacks))

submit(get_top_after_procedure(stacks, procedure, move_by_one=True), part='a')
submit(get_top_after_procedure(stacks, procedure, move_by_one=False), part='b')
