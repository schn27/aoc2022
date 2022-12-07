from aocd import lines
from aocd import submit

root = {'..': None}
current = root

def cd(current, child):
    if child == '/':
        return root

    if not(child in current):
        current[child] = {'..': current}

    return current[child]

read_ls = False

for line in lines:
    if read_ls and line[0] != '$':
        a, b = line.split()
        if a == 'dir':
            cd(current, b)
        else:
            current[b] = int(a)

    else:
        read_ls = False

    if line[0] == '$':
        cmd, *arg = line[2:].split()
        if cmd == 'cd':
            current = cd(current, arg[0])
        else:
            read_ls = True

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
