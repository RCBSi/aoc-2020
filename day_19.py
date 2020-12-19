from common import read_input
import re

def parse_input(raw_in):
    r, m = raw_in
    rules = dict(x.replace('"', '').split(': ') for x in r.split('\n'))
    messages = m.split('\n')
    return rules, messages

def unravel_regex(rules, idx='0'):
    ALLOWED_SINGLE_CHARS = r"^[a-z\|\(\)]$"
    rule = rules.get(idx, idx)

    if re.match(ALLOWED_SINGLE_CHARS, rule):
        return rule
    else:
        if '|' in rule:
            rule = "( " + rule + " )"
        return "".join(unravel_regex(rules, r) for r in rule.split(' '))


def solve_1(rules, messages):
    pattern = "^" + unravel_regex(rules) + "$"
    return sum(True if re.match(pattern, m) else False for m in messages)


def solve_2(raw_in):
    return False


if __name__ == "__main__":
    raw_in = read_input("data/day_19.txt", split_delimiter='\n\n')
    rules, messages = parse_input(raw_in)

    answer_1 = solve_1(rules, messages)
    answer_2 = solve_2(raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
