from common import read_input
import re

REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def parse_dict(user_chunk):
    items = user_chunk.split()
    tmp = [x.split(":") for x in items]
    d = {k: v for k, v in tmp}
    return d


def get_cleaned_input():
    tmp = read_input("data/day_04.txt", split_delimiter="\n\n")
    res = [parse_dict(x) for x in tmp]
    return res


def has_required_fields(d):
    missing_keys = REQUIRED_KEYS - set(d)
    res = missing_keys in (set(), {"cid"})
    return res


def validate_fields(d):
    RULES = {
        "byr": r"*1*",
        "iyr": r"*1*",
        "eyr": r"*1*",
        "hgt": r"*1*",
        "hcl": r"*1*",
        "ecl": r"*1*",
        "pid": r"*1*",
        "cid": r"*1*",
    }

    [(RULES[k], v) for k, v in d.items()]
    [bool(re.match(RULES[k], v)) for k, v in d.items()]

def solve_1(dicts):
    valids = list(filter(has_required_fields, dicts))
    return len(valids)


def solve_2(valids):
    d = valids[0]

    d


if __name__ == "__main__":
    dicts = get_cleaned_input()

    # Part 1
    answer_1 = solve_1(dicts)
    print(f"Part 1 answer: {answer_1}")

    # Part 2
    # answer_2 = solve(inputs)
    # print(f"Part 2 answer: {answer_2}")
