from common import read_input

import numpy as np


def parse_coords(raw_in, ndim):
    coords = set()
    for i, l in enumerate(raw_in):
        for j, c in enumerate(l):
            if c == "#":
                if ndim == 3:
                    coords.add((i, j, 0))
                elif ndim == 4:
                    coords.add((i, j, 0, 0))
    return coords


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

    return set(c for c in candidates if c != loc)


def count_occupied(coords):
    return len(coords)


def update(coords, ndim):
    new = set()

    # Check existing ones first
    for loc in coords:
        n_neighbors = sum((n in coords) for n in get_neighbors(loc, ndim))
        if n_neighbors in (2, 3):
            new.add(loc)
        else:
            if n_neighbors == 3:
                new.add(loc)

    # Then check their neighbors
    possible = set.union(*(get_neighbors(x, ndim) for x in coords))
    for loc in possible:
        n_neighbors = sum((n in coords) for n in get_neighbors(loc, ndim))
        if n_neighbors == 3:
            new.add(loc)

    return new


def solve(raw_in, ndim, sim_length):
    coords = parse_coords(raw_in, ndim)

    for _ in range(sim_length):
        coords = update(coords, ndim)

    return count_occupied(coords)


if __name__ == "__main__":
    raw_in = read_input("data/day_17.txt")

    answer_1 = solve(raw_in, ndim=3, sim_length=6)
    answer_2 = solve(raw_in, ndim=4, sim_length=6)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
