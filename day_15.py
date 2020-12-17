from common import read_input
from collections import defaultdict
from itertools import count

from queue import SimpleQueue

# TODO Use Simplequeue to store histories instead

def solve(raw_in, stop_at):
    ts_iter = count(1)
    history = defaultdict(list, {n: [next(ts_iter)] for n in raw_in})
    spoken = raw_in[-1]
    for ts in ts_iter:
        h = history[spoken]
        # print("......................................")
        # print(f"On turn {ts} we considered {spoken}")
        if len(h) < 2:
            spoken = 0
            history[spoken].append(ts)
            # print("This was the FIRST time it was mentioned, so we say 0")
        else:
            spoken = h[-1] - h[-2]
            history[spoken].append(ts)
            # print(f"It had been spoken previously and the diff was {v}")
        if ts == stop_at:
            return spoken


if __name__ == "__main__":
    raw_in = [int(i) for i in read_input("data/day_15.txt", split_delimiter=',')]

    answer_1 = solve(raw_in, 2020)
    answer_2 = solve(raw_in, 1000000)

    print(f"Part 1 answer: {answer_1}")
    # print(f"Part 2 answer: {answer_2}")

    # 586 ms ± 19.7 ms 