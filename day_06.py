from functools import reduce

from common import read_input


def get_cleaned_input():
    res = [list(map(set, x.split())) for x in read_input("data/day_06.txt", split_delimiter="\n\n")]
    return res


if __name__ == "__main__":
    all_groups = get_cleaned_input()

    get_n_uniques = lambda group: len(reduce(set.union, group))
    get_n_intersected = lambda group: len(reduce(set.intersection, group))

    # Part 1
    answer_1 = sum(get_n_uniques(g) for g in all_groups)
    print(f"Part 1 answer: {answer_1}")

    # Part 2
    answer_2 = sum(get_n_intersected(g) for g in all_groups)
    print(f"Part 2 answer: {answer_2}")
