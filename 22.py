from aocd import data
from aocd import submit
import re
from copy import deepcopy

board, path = data.split('\n\n')

path = list(map(lambda e: int(e) if e.isnumeric() else e, re.findall(r'\d+|[LR]', path)))

board = board.split('\n')

sz = min(map(lambda e: len(e.replace(' ', '')), board))
cols = max(map(len, board)) // sz
rows = len(board) // sz

faces = {}

for r in range(rows):
    y = r * sz
    for c in range(cols):
        x = c * sz
        if x < len(board[y]) and board[y][x] != ' ':
            faces[(x, y)] = [None, None, None, None]

RDLU = ((1, 0), (0, 1), (-1, 0), (0, -1))

for x, y in faces:
    f = faces[(x, y)]

    for i, d in enumerate(RDLU):
        xx = x + sz * d[0]
        yy = y + sz * d[1]
        if (xx, yy) in faces:
            f[i] = ((xx, yy), 0)

def wrap_flat(faces):
    faces = deepcopy(faces)

    for x, y in faces:
        f = faces[(x, y)]
        for i, d in enumerate(RDLU):
            if f[i] is None:
                xx, yy = x, y
                while (xx, yy) in faces:
                    f[i] = ((xx, yy), 0)
                    xx -= d[0] * sz
                    yy -= d[1] * sz

    return faces

def wrap_cube(faces):
    faces = deepcopy(faces)

    done = False

    while not done:
        done = True

        for f in faces.values():
            for i, d in enumerate(RDLU):
                if f[i] is None:
                    third_face, third_rot = None, None

                    for lr in [-1, 1]:
                        lr_face = f[(i + lr) % len(f)]

                        if lr_face is not None:
                            face, rot = lr_face
                            side = (i - rot) % len(f)
                            if faces[face][side] is not None:
                                third_face, third_rot = faces[face][side]
                                third_rot += rot + (-lr)

                    if third_face is not None:
                        f[i] = (third_face, third_rot % len(RDLU))
                        done = False

    return faces

def rotate(x, y, rot):
    if rot == 0:
        return (x, y)
    elif rot == 3:
        return (sz - 1 - y, x)
    elif rot == 2:
        return (sz - 1 - x, sz - 1 - y)
    else:
        return (y, sz - 1 - x)

def move(x, y, d, faces):
    ofs_x, ofs_y = x % sz, y % sz
    dx, dy = RDLU[d]

    xx, yy, dd = x + dx, y + dy, d
    ofs_x, ofs_y = ofs_x + dx, ofs_y + dy

    if (ofs_x < 0 or ofs_x >= sz or ofs_y < 0 or ofs_y >= sz):
        face = ((x // sz) * sz, (y // sz) * sz)
        next_face, rot = faces[face][d]
        ofs_x %= sz
        ofs_y %= sz
        ofs_x, ofs_y = rotate(ofs_x, ofs_y, rot)

        xx, yy = next_face[0] + ofs_x, next_face[1] + ofs_y
        dd = (d - rot) % len(RDLU)

    if board[yy][xx] == '.':
        return xx, yy, dd
    else:
        return x, y, d

def get_password(path, faces):
    x, y = board[0].index('.'), 0
    d = 0

    for p in path:
        if isinstance(p, int):
            for _ in range(p):
                x, y, d = move(x, y, d, faces)
        else:
            d = (d + (1 if p == 'R' else -1)) % len(RDLU)

    return (y + 1) * 1000 + 4 * (x + 1) + d

submit(get_password(path, wrap_flat(faces)), part='a')
submit(get_password(path, wrap_cube(faces)), part='b')
