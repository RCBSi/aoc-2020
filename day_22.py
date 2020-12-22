from itertools import count

from common import read_input


def parse_input(raw_in):
    parse = lambda p: [int(x) for x in p.split(":")[1].split()]
    return [parse(p) for p in raw_in]


def solve_1(decks):
    while (len(decks[0]) > 0) & (len(decks[1]) > 0):
        a, a_ = decks[0][0], decks[0][1:]
        b, b_ = decks[1][0], decks[1][1:]
        decks = [a_ + [a, b], b_] if (a > b) else [a_, b_ + [b, a]]
    winner_deck = decks[0] if len(decks[1]) == 0 else decks[1]
    score = sum(m * c for m, c in zip(count(1), winner_deck[::-1]))
    return score


def solve_2(raw_in):
    return False


if __name__ == "__main__":
    raw_in = read_input("data/day_22.txt", split_delimiter="\n\n")
    decks = parse_input(raw_in)

    answer_1 = solve_1(decks)
    answer_2 = solve_2(raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
