from aocd import lines
from aocd import submit
import re

def parse_line(line):
    numbers = tuple(map(int, re.findall(r'\d+', line)))
    return {
        'id': numbers[0],
        'requires': [(numbers[1], 0, 0, 0), (numbers[2], 0, 0, 0), (numbers[3], numbers[4], 0, 0), (numbers[5], 0, numbers[6], 0)]}

blueprints = list(map(parse_line, lines))

def can_buy(minerals, requires):
    return all(map(lambda e: e[0] - e[1] >= 0, zip(minerals, requires)))

def get_remaining(minerals, requires):
    return tuple(map(lambda e: e[0] - e[1], zip(minerals, requires)))

def get_max(bp, time):
    states = [((1, 0, 0, 0), (0, 0, 0, 0))]
    seen = set()

    for t in range(time):
        new_states = []
        for robots, minerals in states:
            seen.add(robots)
            for r in range(3, -1, -1):
                if can_buy(minerals, bp['requires'][r]):
                    remaining = get_remaining(minerals, bp['requires'][r])
                    new_robots = [*robots]
                    new_robots[r] += 1
                    new_robots = tuple(new_robots)
                    if not new_robots in seen:
                        new_minerals = tuple(map(lambda e: e[0] + e[1], zip(remaining, robots)))
                        new_states.append((new_robots, new_minerals))
                        if r == 3 or r == 2:
                            break

            new_minerals = tuple(map(lambda e: e[0] + e[1], zip(minerals, robots)))
            new_states.append((tuple(robots), new_minerals))

        states = new_states
    return max(map(lambda e: e[1][-1], states))

print('be patient...')

submit(sum(map(lambda e: e['id'] * get_max(e, 24), blueprints)), part='a')
submit(get_max(blueprints[0], 32) * get_max(blueprints[1], 32) * get_max(blueprints[2], 32), part='b')
