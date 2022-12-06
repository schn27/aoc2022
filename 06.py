from aocd import data
from aocd import submit

def get_marker_pos(buf, n):
    for i in range(len(buf) - n):
        if (len(set(buf[i: i + n])) == n):
            return i + n
    return -1

submit(get_marker_pos(data, 4), part='a')
submit(get_marker_pos(data, 14), part='b')
