from aocd import data
from aocd import submit
import re
import copy

state, procedure = map(lambda e: e.split("\n"), data.split("\n\n"))

nstacks = int(re.findall("\d+", state[-1])[-1])
stacks = [[] for _ in range(nstacks)]

for line in state[:-1]:
    for i in range(nstacks):
        c = line[i * 4 + 1]
        if c.isalpha():
            stacks[i].append(c)

procedure = list(map(lambda e: list(map(int, re.findall("\d+", e))), procedure))

def get_top_after_procedure(stacks, procedure, *, reversed):
    stacks = copy.deepcopy(stacks)

    for n, src, dst in procedure:
        p = stacks[src - 1][:n]
        stacks[src - 1] = stacks[src - 1][n:]
        if reversed:
            p.reverse()
        stacks[dst - 1] = p + stacks[dst - 1]

    return "".join(map(lambda e: e[0], stacks))

submit(get_top_after_procedure(stacks, procedure, reversed=True), part="a")
submit(get_top_after_procedure(stacks, procedure, reversed=False), part="b")
