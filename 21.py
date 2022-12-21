from aocd import lines
from aocd import submit

monkeys = {}

for line in lines:
    l, r = line.split(': ')
    monkeys[l] = int(r) if r.isnumeric() else r.split(' ')

def get_root(monkeys):
    monkeys = monkeys.copy()
    unknown = set(map(lambda e: e[0], filter(lambda e: isinstance(e[1], list), monkeys.items())))

    while 'root' in unknown:
        new_unknown = set()
        for monkey in unknown:
            m1, op, m2 = monkeys[monkey]
            if not (m1 in unknown) and not (m2 in unknown):
                m1, m2 = monkeys[m1], monkeys[m2]
                res = m1 + m2 if op == '+' else m1 - m2 if op == '-' else m1 * m2 if op == '*' else m1 // m2
                monkeys[monkey] = res
            else:
                new_unknown.add(monkey)
        unknown = new_unknown

    return monkeys['root']

def get_humn(monkeys):
    monkeys['root'][1] = '-'
    res1 = get_root(monkeys)

    bit = 1
    while bit < abs(res1):
        bit *= 2

    monkeys['humn'] = bit

    res2 = get_root(monkeys)
    invert = res1 > res2

    guess = 0
    while bit:
        monkeys['humn'] = guess + bit
        res = get_root(monkeys) * (-1 if invert else 1)
        if res <= 0:
            guess += bit
        bit //= 2

    return guess

submit(get_root(monkeys), part='a')
submit(get_humn(monkeys), part='b')
