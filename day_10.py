from functools import lru_cache

import numpy as np

from common import read_input


def get_ordered_joltages():
    res = [int(x) for x in read_input("data/day_10.txt")]
    s = sorted(res)
    a = tuple([0] + s + [max(s) + 3])
    return a


def solve_1(joltages):
    diffs = np.diff(joltages)
    return sum(diffs == 1) * sum(diffs == 3)


def get_antecedent_idxes(adapter_idx, joltages):
    candidates = [(adapter_idx - i) for i in (1, 2, 3) if (adapter_idx - i) >= 0]
    valid = [c for c in candidates if (joltages[adapter_idx] - joltages[c]) <= 3]
    return valid


@lru_cache(maxsize=None)
def get_n_paths(adapter_idx, joltages):
    if adapter_idx == 0:
        return 1
    else:
        antecedent_idxs = get_antecedent_idxes(adapter_idx, joltages)
        return sum(get_n_paths(a, joltages) for a in antecedent_idxs)


if __name__ == "__main__":
    joltages = tuple(get_ordered_joltages())

    # Part 1
    answer_1 = solve_1(joltages)
    print(f"Part 1 answer: {answer_1}")

    # Part 2
    max_adapter_idx = len(joltages) - 1
    answer_2 = get_n_paths(max_adapter_idx, joltages)
    print(f"Part 2 answer: {answer_2}")