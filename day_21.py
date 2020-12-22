from collections import defaultdict
from copy import deepcopy

from common import read_input


def parse_inputs(raw_in):
    foods = []
    for line in raw_in:
        i, a = line[:-1].split(" (contains ")
        ingredients = set(i.split())
        allergens = set(a.split(", "))
        foods.append((ingredients, allergens))
    return foods


def _build_lookups(foods):
    ingt_holders = defaultdict(set)
    allg_holders = defaultdict(set)

    for idx, f in enumerate(foods):
        ingredients, allergens = f
        for allg in allergens:
            allg_holders[allg].add(idx)
        for ingt in ingredients:
            ingt_holders[ingt].add(idx)

    return dict(ingt_holders), dict(allg_holders)


def solve(foods):
    unsolved = deepcopy(foods)
    solution = {}

    while any(len(x[1]) > 0 for x in unsolved):
        updates = []
        ingt_holders, allg_holders = _build_lookups(unsolved)

        # Check if common ingredients
        interesting_allgs = [a for a, hs in allg_holders.items() if len(hs) >= 2]
        for allg in interesting_allgs:
            holders = allg_holders[allg]
            common_ingts = set.intersection(*(unsolved[f][0] for f in holders))
            common_allgs = set.intersection(*(unsolved[f][1] for f in holders))
            if len(common_allgs) == len(common_ingts) == 1:
                updates.append((common_ingts.pop(), common_allgs.pop()))

        # Check certainties
        for f in unsolved:
            if len(f[0]) == len(f[1]) == 1:
                updates.append(tuple(list(x)[0] for x in f))

        # Update found solutions
        for ingt, allg in updates:
            solution[ingt] = allg
            for f in ingt_holders[ingt]:
                unsolved[f][0].remove(ingt)
            for f in allg_holders[allg]:
                unsolved[f][1].remove(allg)

    answer_1 = sum(len(x[0]) for x in unsolved)
    answer_2 = ",".join(sorted(solution, key=solution.get))

    return answer_1, answer_2


if __name__ == "__main__":
    raw_in = read_input("data/day_21.txt")
    foods = parse_inputs(raw_in)

    answer_1, answer_2 = solve(foods)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
