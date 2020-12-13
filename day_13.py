from itertools import count

import numpy as np

from common import read_input


def solve_1(raw_in):
    a, b = raw_in

    earliest = int(a)
    bus_ids = [int(x) for x in b.split(',') if x != 'x']

    wait_times = np.array([x - (earliest % x) for x in bus_ids])

    min_id = np.argmin(wait_times)

    return wait_times[min_id] * bus_ids[min_id]


def get_wait_time(ts, bus_id):
    return (bus_id - ts % bus_id)

def solve_2(raw_in):
    _, b = raw_in
    buses = [(int(b), a) for a, b in enumerate(b.split(','), 0) if b != 'x']
    buses[0] = (buses[0][0], buses[0][0])
    buses = sorted(buses)

    min_so_far = 0
    step = 1 
    for bus_id, condition in buses:
        # print(".................")
        # print(f"bus_id {bus_id}, condition {condition}, min so far {min_so_far}")
        
        # a = (condition + min_so_far*step)/bus_id
        # print(a)
        for tryout in count(min_so_far, step):
            # tryout = next(i2)

            to_wait = get_wait_time(tryout, bus_id)
            # print(f"Tryout:{tryout}, step {step}, time to wait {to
            # _wait}")

            # print(f"Trying {tryout} with bus_id {bus_id} and step {step} => next leaves in {to_wait}")
            if (to_wait == condition) | (condition % bus_id == to_wait):
                new_step = np.lcm(step, bus_id)
                # print(f"Condition fulfilled, upgrading step from {step} to {new_step}")
                step = new_step
                min_so_far = tryout
                break
    # print(tryout)
    
    return tryout



if __name__ == "__main__":
    raw_in = read_input("data/day_13.txt")

    answer_1 = solve_1(raw_in)
    answer_2 = solve_2(raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
