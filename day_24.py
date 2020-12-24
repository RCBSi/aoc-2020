from common import read_input

import re

COORDS = {
    "e": (0, 2),
    "se": (-2, 1),
    "sw": (-2, -1),
    "w": (0, -2),
    "nw": (2, -1),
    "ne": (2, 1),
}


def parse_instructions(raw_in):
    parse_line = lambda line: [x for x in re.findall(r'(e|se|sw|w|nw|ne)', line)]
    return [parse_line(line) for line in raw_in]


def create_floor(instructions):
    blacks = set()
    for path in instructions:
        x, y = (0,0)
        for c in path:
            dx, dy = COORDS[c]
            x += dx
            y += dy
        if (x, y) in blacks:
            blacks.remove((x, y))
        else:
            blacks.add((x, y))
    return blacks


def solve_2(raw_in):
    return False


if __name__ == "__main__":
    raw_in = read_input("data/day_24.txt")
    instructions = parse_instructions(raw_in)

    floor = create_floor(instructions)

    answer_1 = len(floor)
    answer_2 = solve_2(raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
