import re
from collections import defaultdict
from functools import reduce

from common import read_input


def parse_type_and_amount(c):
    as_list = c.split()
    amount = int(as_list[0])
    bag_type = " ".join(as_list[1:])
    return (bag_type, amount)


def parse_rule(rule):
    tmp = rule.replace(".", "").replace("bags", "bag")
    holder, contents_str = tmp.split(" contain ")

    if contents_str == "no other bag":
        d = {}
    else:
        contents = [b.strip() for b in contents_str.split(",")]
        d = {k: v for k, v in map(parse_type_and_amount, contents)}
    return (holder, d)


class Bag:
    def __init__(self, name):
        self.name = name
        self.parents = {}
        self.children = {}

    def __repr__(self):
        return f"{self.name}"


def get_bag_graph():
    raw = [x for x in read_input("data/day_07.txt")]

    bags = {}
    for line in raw:
        parent, children = parse_rule(line)
        if parent not in bags:
            bags[parent] = Bag(parent)
        for child, n in children.items():
            if child not in bags:
                bags[child] = Bag(child)
            bags[parent].children[child] = n
            bags[child].parents[parent] = n
    return bags


def get_unique_ancestors(bag_graph, bag_name):
    if bag_graph[bag_name].parents == {}:
        return set()
    else:
        direct_ancestors = set(bag_graph[bag_name].parents)
        further_ancestors = reduce(
            set.union,
            [get_unique_ancestors(bag_graph, k) for k in bag_graph[bag_name].parents],
        )
        return direct_ancestors | further_ancestors


def calculate_decendants(bag_graph, bag_name):
    if bag_graph[bag_name].children == {}:
        return 0
    else:
        n_children = sum(v for v in bag_graph[bag_name].children.values())
        n_further_descendants = sum(
            v * calculate_decendants(bag_graph, k)
            for k, v in bag_graph[bag_name].children.items()
        )
        return n_children + n_further_descendants


if __name__ == "__main__":
    bag_graph = get_bag_graph()

    # Part 1
    answer_1 = get_unique_ancestors(bag_graph, "shiny gold bag")
    print(f"Part 1 answer: {len(answer_1)}")

    # Part 2
    answer_2 = calculate_decendants(bag_graph, "shiny gold bag")
    print(f"Part 2 answer: {answer_2}")