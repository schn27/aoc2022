from aocd import lines
from aocd import submit

dirs = {'': 0}
current = ['']

for line in lines:
    w = line.split()
    if w[0] == '$':
        if w[1] == 'cd':
            if w[2] == '/':
                current = ['']
            elif w[2] == '..':
                current = current[:-1]
            else:
                current.append(w[2])
    elif w[0] != 'dir':
        for i in range(len(current)):
            dir_name = '/'.join(current[:i + 1])
            dirs[dir_name] = int(w[0]) + (dirs[dir_name] if dir_name in dirs else 0)

sizes = list(sorted(dirs.values()))

submit(sum(filter(lambda e: e <= 100000, sizes)), part='a')

goal = 30000000 - (70000000 - sizes[-1])

submit(next(filter(lambda e: e >= goal, sizes)), part='b')
