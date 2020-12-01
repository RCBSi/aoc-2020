from common import read_input
from itertools import combinations
from functools import reduce
from operator import mul


def get_cleaned_input():
    res = [int(x) for x in read_input("data/day_01.txt")]
    return res


def solve(numbers, combination_length):
    for tryout in combinations(numbers, combination_length):
        if sum(tryout) == 2020:
            return reduce(mul, tryout)
    print("Answer not found")


if __name__ == "__main__":
    entries = get_cleaned_input()

    # Part 1
    answer_1 = solve(entries, combination_length=2)
    print(f"Part 1 answer: {answer_1}")

    # Part 2
    answer_2 = solve(entries, combination_length=3)
    print(f"Part 2 answer: {answer_2}")
