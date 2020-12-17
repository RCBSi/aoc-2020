from common import read_input

import numpy as np

# TODO Clean up
# 1) Store as a set instead
# 2) Clean up

def parse_coords(raw_in, ndim):
    coords = {}
    for i, l in enumerate(raw_in):
        for j, c in enumerate(l):
            if c == "#":
                if ndim == 3:
                    coords[(i, j, 0)] = c
                elif ndim == 4:
                    coords[(i, j, 0, 0)] = c
    return coords


# def print_coords(coords, z_layer):
#     layer = []
#     for k in coords.keys():
#         if k[2] == z_layer:
#             layer.append((k[0], k[1]))
#     a = np.array(layer)
#     xmin, xmax = min(a[:, 0]), max(a[:, 0])
#     ymin, ymax = min(a[:, 1]), max(a[:, 1])

#     s = ""
#     for x in range(xmin, xmax+1):
#         for y in range(ymin, ymax+1):
#             s += coords.get((x, y, z_layer), '.')
#         s += "\n"
#     print(s)


def get_neighbors(loc, ndim):
    if ndim == 3:
        x, y, z = loc
        candidates = (
            (x + a, y + b, z + c)
            for a in (-1, 0, 1)
            for b in (-1, 0, 1)
            for c in (-1, 0, 1)
        )
    if ndim == 4:
        x, y, z, w = loc
        candidates = (
            (x + a, y + b, z + c, w + d)
            for a in (-1, 0, 1)
            for b in (-1, 0, 1)
            for c in (-1, 0, 1)
            for d in (-1, 0, 1)
        )

    return (c for c in candidates if c != loc)


def count_occupied(coords):
    return len(coords)


def update(coords, ndim):
    new = {}
    # Get list of nodes and their neighbors
    old_keys = set(coords.keys())
    neighbors = set.union(*(set(get_neighbors(x, ndim)) for x in old_keys))

    for loc in old_keys:
        v = coords.get(loc, ".")
        n_neighbors = sum(coords.get(n, ".") == "#" for n in get_neighbors(loc, ndim))
        if v == "#":
            if n_neighbors in (2, 3):
                new[loc] = "#"
        else:
            if n_neighbors == 3:
                new[loc] = "#"

    for loc in neighbors:
        v = coords.get(loc, ".")
        n_neighbors = sum(coords.get(n, ".") == "#" for n in get_neighbors(loc, ndim))

        if n_neighbors == 3:
            new[loc] = "#"

    return new


def solve(raw_in, ndim):
    coords = parse_coords(raw_in, ndim)

    for _ in range(6):
        coords = update(coords, ndim)

    return count_occupied(coords)


def solve_2(raw_in):
    return False


if __name__ == "__main__":
    raw_in = read_input("data/day_17.txt")

    # coords = update(coords)
    # print_coords(coords, 0)

    answer_1 = solve(raw_in, ndim=3)
    answer_2 = solve(raw_in, ndim=4)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
