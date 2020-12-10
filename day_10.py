from functools import reduce
from math import factorial
from operator import mul

import numpy as np

from common import read_input


def get_ordered_joltages():
    res = [int(x) for x in read_input("data/day_10.txt")]
    s = sorted(res)
    a = np.array([0] + s + [max(s) + 3])
    return np.array(a)


def solve_1(diffs):
    return sum(diffs == 1) * sum(diffs == 3)


def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def n_th_triangle_number(n):
    return binomial_coefficient(n + 1, 2)


def number_of_combos(diff_chunk):
    # TODO This function works correctly only if
    # there are no number 2's in diff_chunk
    if len(diff_chunk) < 2:
        res = 1
    else:
        res = n_th_triangle_number(len(diff_chunk) - 1) + 1
    return res


def solve_2(diffs):
    as_str = "".join(str(x) for x in diffs)
    diff_chunks = [x for x in as_str.split("3") if x != ""]

    n_combos = [number_of_combos(c) for c in diff_chunks]
    res = int(reduce(mul, n_combos))
    return res


if __name__ == "__main__":
    joltages = get_ordered_joltages()
    diffs = np.diff(joltages)

    # Part 1
    answer_1 = solve_1(diffs)
    print(f"Part 1 answer: {answer_1}")

    # Part 2
    answer_2 = solve_2(diffs)
    print(f"Part 2 answer: {answer_2}")
