from functools import reduce
from operator import mul
from itertools import cycle

import numpy as np

from common import array_to_string, read_input, str_to_array

OPPOSITE_HDG = {"n": "s", "e": "w", "s": "n", "w": "e"}


class Tile:
    def __init__(self, id, array):
        self.id = id
        self.arr = array

    def __repr__(self):
        return f"Tile {self.id}\n{array_to_string(self.arr)}"

    def rotate(self):
        self.arr = np.rot90(self.arr)

    def flip(self):
        self.arr = np.flip(self.arr, axis=1)

    def get_edges(self):
        return {
            "n": "".join(map(chr, self.arr[0, :])),
            "s": "".join(map(chr, self.arr[-1, :])),
            "w": "".join(map(chr, self.arr[:, 0])),
            "e": "".join(map(chr, self.arr[:, -1])),
        }


def create_tiles_dict(raw_in):
    tiles_dict = {}

    for line in raw_in:
        a, b = line.split("\n", maxsplit=1)
        a = int(a[5:-1])
        b = str_to_array(b.split())
        tiles_dict[a] = Tile(a, b)

    return tiles_dict


def get_corner_tiles(tiles_dict):
    # TODO Clean up
    tiles = list(tiles_dict.values())
    corner_pieces = []
    for t in tiles:
        s = 0
        for e in t.get_edges().values():
            others = set.union(
                *(set(t2.get_edges().values()) for t2 in tiles if (t != t2))
            )
            others_flipped = set(x[::-1] for x in others)
            if (e in others) or (e in others_flipped):
                s += 1
        if s == 2:
            corner_pieces.append(t.id)

    return corner_pieces


def find_match(tile, hdg, unsolved_tiles, tiles_dict):
    opp_hdg = OPPOSITE_HDG[hdg]
    for tile_id in unsolved_tiles:
        other = tiles_dict[tile_id]
        if tile == other:
            print("We have a BIG BUG")
        for _ in range(2):
            for _ in range(4):
                if tile.get_edges()[hdg] == other.get_edges()[opp_hdg]:
                    return other
                other.rotate()
            other.flip()


def piece_together(tiles_dict, corner_tiles):
    # Resources
    LOC_OFFSET = {
        "n": np.array([-1, 0]),
        "e": np.array([0, 1]),
        "s": np.array([1, 0]),
        "w": np.array([0, -1]),
    }
    hdg_iter = cycle(["e", "s", "w", "n"])

    # Init
    unsolved_tiles = set(tiles_dict)
    solution = {}
    loc = np.array([0, 0])
    hdg = next(hdg_iter)
    tile = tiles_dict[corner_tiles[0]]
    unsolved_tiles.remove(tile.id)

    # Loop and build the solution dict
    while unsolved_tiles:
        solution[tuple(loc)] = tile
        match = find_match(tile, hdg, unsolved_tiles, tiles_dict)
        if match:
            # print(f"Found next tile {match.id}")
            tile = match
            unsolved_tiles.remove(tile.id)
            loc += LOC_OFFSET[hdg]

        if not match:
            # print("Direction finished, changing dir")
            hdg = next(hdg_iter)
    solution[tuple(loc)] = tile

    # Transform solution dict into a big tile
    row_idxes, col_idxes = zip(*solution.keys())
    row_min, row_max = min(row_idxes), max(row_idxes)
    col_min, col_max = min(col_idxes), max(col_idxes)
    rows = []
    for col in range(col_min, col_max + 1):
        rows.append(
            np.concatenate(
                [
                    solution[(row, col)].arr[1:-1, 1:-1]
                    for row in range(row_min, row_max + 1)
                ],
                axis=0,
            )
        )
    final = np.concatenate(rows, axis=1)

    return Tile("FINALE", final)


def get_roughness(array):
    serpent_ascii = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    serpent_filter = (str_to_array(serpent_ascii) == ord("#")).astype(int)
    serpent_y_len, serpent_x_len = serpent_filter.shape

    hashes = (array == ord("#")).astype(int)

    solution = np.zeros_like(hashes)
    max_y, max_x = solution.shape
    for row in range(0, max_y-serpent_y_len+1):
        for col in range(0, max_x-serpent_x_len+1):
            original = hashes[row:row+serpent_y_len, col:col+serpent_x_len]
            filtered = original * serpent_filter
            if np.array_equal(filtered, serpent_filter):
                solution[row:row+serpent_y_len, col:col+serpent_x_len] += filtered
    
    roughness = np.sum((solution == 0) * hashes)
    return roughness

def solve_2(tiles_dict, corner_tiles):
    final = piece_together(tiles_dict, corner_tiles)

    roughnesses = []
    for _ in range(2):
        final.flip()
        for _ in range(4):
            final.rotate()
            r = get_roughness(final.arr)
            roughnesses.append(r)

    return min(roughnesses)


if __name__ == "__main__":
    raw_in = read_input("data/day_20.txt", split_delimiter="\n\n")
    tiles_dict = create_tiles_dict(raw_in)

    corner_tiles = get_corner_tiles(tiles_dict)
    answer_2 = solve_2(tiles_dict, corner_tiles)

    print(f"Part 1 answer: {reduce(mul, corner_tiles)}")
    print(f"Part 2 answer: {answer_2}")
