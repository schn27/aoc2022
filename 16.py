from aocd import lines
from aocd import submit
import re
from itertools import combinations

graph = dict(map(lambda e: (e[0], [int(e[1]), e[2:]]), map(lambda e: list(re.findall(r'[A-Z]{2}|\d+', e)), lines)))

path_memo = {}

def get_path(node1, node2):
    if node1 + node2 in path_memo:
        return path_memo[node1 + node2]

    visited = set()
    queue = [(node1, 0)]
    length = None

    while len(queue) > 0:
        n, d = queue[0]
        queue = queue[1:]
        visited.add(n)

        if n == node2:
            length = d if length is None else min(length, d)
        else:
            d += 1
            if length is None or d < length:
                queue += list(map(lambda e: (e, d), filter(lambda e: not e in visited, graph[n][1])))

    path_memo[node1 + node2] = length
    return length

valves = [k for k in graph if graph[k][0] > 0]

def get_max_pressure(node, time, valves):
    if len(valves) == 0:
        return 0

    pressure = 0

    for i, v in enumerate(valves):
        new_time = max(0, time - get_path(node, v) - 1)
        if new_time != 0:
            pressure = max(pressure, graph[v][0] * new_time + get_max_pressure(v, new_time, valves[:i] + valves[i+1:]))

    return pressure

def get_max_pressure2(node, time, valves):
    max_pressure = 0
    for combs in (combinations(valves, r) for r in range(len(valves) // 2, len(valves))):
        for comb in combs:
            comb2 = list(set(valves[:]) - set(comb))
            max_pressure = max(max_pressure, get_max_pressure(node, time, list(comb)) + get_max_pressure(node, time, comb2))
    return max_pressure

submit(get_max_pressure('AA', 30, valves), part='a')
submit(get_max_pressure2('AA', 26, valves), part='b')
