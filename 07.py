from aocd import lines
from aocd import submit

root = {}
current = root

def cd(current, child):
    if child == '/':
        return root

    if not(child in current):
        current[child] = {'..': current}

    return current[child]

for line in lines:
    w = line.split()
    if w[0] == '$':
        if w[1] == 'cd':
            current = cd(current, w[2])
    elif w[0] != 'dir':
        current[w[1]] = int(w[0])

def get_sizes(current, sizes):
    total = 0

    for k, v in current.items():
        if k != '..':
            total += v if isinstance(v, int) else get_sizes(v, sizes)

    sizes.append(total)
    return total

sizes = []
total_size = get_sizes(root, sizes)

submit(sum(filter(lambda e: e <= 100000, sizes)), part='a')

sizes.sort()
goal = 30000000 - (70000000 - total_size)

submit(next(filter(lambda e: e >= goal, sizes)), part='b')
