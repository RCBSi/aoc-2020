import re

from common import read_input


def parse_type_and_amount(c):
    as_list = c.split()
    amount = int(as_list[0])
    bag_type = " ".join(as_list[1:])
    return (bag_type, amount)


def parse_rule(rule):
    cleaned = rule.replace(".", "").replace("bags", "bag")
    holder, contents_str = cleaned.split(" contain ")

    if contents_str == "no other bag":
        d = {}
    else:
        contents = [b.strip() for b in contents_str.split(",")]
        d = {k: v for k, v in map(parse_type_and_amount, contents)}
    return (holder, d)


def get_rules():
    raw = [x for x in read_input("data/day_07.txt")]
    d = dict(parse_rule(r) for r in raw)
    return d


def create_ancestry_dict(rules):
    d = {b: set() for b in rules}
    for b, children in rules.items():
        for c in children:
            d[c].add(b)
    return d


def get_unique_ancestors(rules, bag_name):
    ancestors = create_ancestry_dict(rules)
    if ancestors[bag_name] == set():
        return set()
    else:
        parents = ancestors[bag_name]
        further_ancestors = set.union(
            *(get_unique_ancestors(rules, b) for b in ancestors[bag_name])
        )
        return parents | further_ancestors


def calculate_decendants(rules, bag_name):
    if rules[bag_name] == {}:
        return 0
    else:
        n_children = sum(v for v in rules[bag_name].values())
        n_further_descendants = sum(
            v * calculate_decendants(rules, k) for k, v in rules[bag_name].items()
        )
        return n_children + n_further_descendants


if __name__ == "__main__":
    rules = get_rules()

    # Part 1
    unique_ancestors = get_unique_ancestors(rules, "shiny gold bag")
    print(f"Part 1 answer: {len(unique_ancestors)}")

    # Part 2
    answer_2 = calculate_decendants(rules, "shiny gold bag")
    print(f"Part 2 answer: {answer_2}")
