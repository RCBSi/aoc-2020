from copy import deepcopy
from functools import reduce
from operator import mul

import numpy as np

from common import read_input


def _range_to_set(rng):
    l, h = map(int, rng.split("-"))
    return set(i for i in range(l, h + 1))


def _parse_validity(line):
    a, b = line.split(": ")
    valids = reduce(set.union, (_range_to_set(x) for x in b.split(" or ")))
    return (a, valids)


def parse_input(raw_in):
    r, m, o = [x.split("\n") for x in raw_in]

    rules = dict(_parse_validity(x) for x in r)

    to_set = lambda l: tuple(int(x) for x in l.split(","))
    mine = to_set(m[1])
    others = [to_set(x) for x in o[1:]]

    return rules, mine, others


def get_valid_tickets(rules, tickets):
    invalids = set()
    error_rate = 0
    for ticket in tickets:
        for n in ticket:
            if all([(n not in vs) for vs in rules.values()]):
                # print(n, " is not valid")
                error_rate += n
                invalids.add(ticket)

    valids = set(tickets) - invalids
    return valids, invalids, error_rate


# def get_valid_children(n, rules, valids):
#     rule_names = list(rules.keys())
#     possible_final = set(range(0, len(rules))) - set(n)
#     potential = [tuple(list(n)+[x]) for x in possible_final]

#     if not potential:
#         return

#     children = set()
#     for p in potential:
#         # print(f"Checking potential for {p}")
#         rule_name = rule_names[p[-1]]
#         # print(f"Rule name {rule_name}")
#         if all([o[len(p)-1] in rules[rule_name] for o in valids]):
#             # print(f"Appended {p}")
#             children.add(p)
#     # if len(children) == 0:
#     #     print(f"No valid children for {n}")
#     return list(children)


# def is_final(n, rules):
#     return len(n) == len(rules)

# def dfs(rules, valids):
#     stack = []
#     visited = set()

#     stack.extend(get_valid_children(tuple(), rules, valids))

#     i = 0
#     while len(stack) > 0:
#         n = stack.pop()
#         # print("............")
#         # print(f"Looking at {n}")
#         if n not in visited:
#             visited.add(n)
#             if is_final(n, rules):
#                 # print("Found answer")
#                 return n
#             else:
#                 children = get_valid_children(n, rules, valids)
#                 stack.extend(children)
#         i += 1
#         if i%50000 == 0:
#             print(f"On iteration {i}, stack size {len(stack)}, last checked {n}")


def build_possibilities_dict(rules, valids):
    possibilities = {}
    tickets = np.array(list(valids))

    for r, vrange in rules.items():
        res = set()
        for i, _ in enumerate(rules):
            if all(v in vrange for v in tickets[:, i]):
                res.add(i)
        possibilities[r] = res
    return possibilities


def eliminate(possibilities):
    pdict = deepcopy(possibilities)
    solved = {}
    # Collect stuff to be eliminated
    while True:
        remove_keys = set()
        remove_values = set()
        for r, ps in pdict.items():
            if len(ps) == 1:
                solved[r] = sum(ps)
                remove_keys.add(r)
                remove_values |= ps
        if len(remove_keys) + len(remove_values) == 0:
            break
        # Remove
        pdict = {
            k: (v - remove_values) for k, v in pdict.items() if k not in remove_keys
        }
    return solved


def solve_2(rules, mine, valids):
    possibilities = build_possibilities_dict(rules, valids)
    solved = eliminate(possibilities)
    idxes = [v for k, v in solved.items() if k.startswith("departure")]
    
    return reduce(mul,[mine[i] for i in idxes])


if __name__ == "__main__":
    raw_in = read_input("data/day_16.txt", split_delimiter="\n\n")
    rules, mine, others = parse_input(raw_in)

    valids, invalids, error_rate = get_valid_tickets(rules, others)
    answer_2 = solve_2(rules, mine, valids)

    print(f"Part 1 answer: {error_rate}")
    print(f"Part 2 answer: {answer_2}")
