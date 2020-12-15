from common import read_input
from collections import defaultdict
from itertools import count

from queue import SimpleQueue

def solve(raw_in, stop_at):
    ts_iter = count(1)
    # spoken = raw_in[:]
    history = defaultdict(list, {n: [next(ts_iter)] for n in raw_in})
    spoken = raw_in[-1]
    for ts in ts_iter:
        h = history.get(spoken)
        # print("......................................")
        # print(f"On turn {ts} we considered {spoken}")
        if len(h) < 2:
            v = 0
            # print("This was the FIRST time it was mentioned, so we say 0")
        else:
            v = h[-1] - h[-2]
            # print(f"It had been spoken previously and the diff was {v}")
        spoken = v
        history[v].append(ts)

        if ts == stop_at:
            return spoken


if __name__ == "__main__":
    raw_in = [int(i) for i in read_input("data/day_15.txt", split_delimiter=',')]

    answer_1 = solve(raw_in, 2020)
    # answer_2 = solve(raw_in, 100000)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")

    #55.7 ms ± 4.75 