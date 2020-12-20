from functools import reduce
from operator import mul

import numpy as np

from common import array_to_string, read_input, str_to_array


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
        e1 = "".join(map(chr, self.arr[0,:]))
        e2 = "".join(map(chr, self.arr[-1,:]))
        e3 = "".join(map(chr, self.arr[:, 0]))
        e4 = "".join(map(chr, self.arr[:, -1]))
        return (e1, e2, e3, e4)


def create_tiles(raw_in):
    tiles = []

    for line in raw_in:
        a, b = line.split('\n', maxsplit=1)
        a = int(a[5:-1])
        b = str_to_array(b.split())
        tiles.append(Tile(a, b))

    return tiles 



def solve_1(tiles):
    t = tiles[0]

    corner_pieces = []
    for t in tiles:
        s = 0
        for e in t.get_edges():
            others = set.union(*(set(t2.get_edges()) for t2 in tiles if (t != t2)))
            others_flipped = set(x[::-1] for x in others)
            if (e in others) or (e in others_flipped):
                s += 1
        if s == 2:
            corner_pieces.append(t.id)

    return reduce(mul, corner_pieces)



def solve_2(raw_in):
    return False


if __name__ == "__main__":
    raw_in = read_input("data/day_20.txt", split_delimiter="\n\n")
    tiles = create_tiles(raw_in)

    answer_1 = solve_1(tiles)
    answer_2 = solve_2(raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
