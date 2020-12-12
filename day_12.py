from common import read_input
import numpy as np

from itertools import cycle

def get_cleaned_input():
    res = [x for x in read_input("data/day_12.txt")]
    return res

def _get_next_hdg(hdg):
    pass

def parse_action(s):
    return s[0], int(s[1:])

DIRS = {
    'N': np.array([0, 1]),
    'E': np.array([1, 0]),
    'S': np.array([0, -1]),
    'W': np.array([-1, 0]),
}

import math

def _rotate_wpt(point, cmd, value):
    v = int(value/90)
    if cmd == 'R':
        v *= -1
    cp = complex(*point)
    new = (1j **v )* cp
    return np.array((round(new.real), round(new.imag)))

def _get_next_hdg(hdg, cmd, value):
    "".join(DIRS.keys())

    if cmd == 'R':
        it = cycle("".join(DIRS.keys()))
    else:
        it = cycle("".join(DIRS.keys())[::-1])

    for i in it:
        if i == hdg:
            for _ in range(int(value/90)):
                v = next(it)
            return v         

class SimpleShip:
    def __init__(self):
        self.pos = np.array([0,0])
        self.hdg = 'E'

    def update(self, action):
        cmd, value = parse_action(action)

        if cmd in 'NSEW':
            self.pos += value*DIRS[cmd]
        elif cmd in "LR":
            self.hdg = _get_next_hdg(self.hdg, cmd, value)
        elif cmd == 'F':
            self.pos += value*DIRS[self.hdg]


class ComplexShip:
    def __init__(self):
        self.pos = np.array([0,0])
        self.wpt = np.array([10, 1])

    def update(self, action):
        cmd, value = parse_action(action)

        if cmd in 'NSEW':
            self.wpt += value*DIRS[cmd]
        elif cmd in "LR":
            self.wpt = _rotate_wpt(self.wpt, cmd, value)
        elif cmd == 'F':
            self.pos += value*self.wpt



if __name__ == "__main__":
    inputs = get_cleaned_input()


    s = SimpleShip()

    for a in inputs:
        s.update(a)

    
    # Part 1
    # answer_1 = solve(inputs)
    print(f"Part 1 answer: {sum(abs(a) for a in s.pos)}")

    # Part 2
    c = ComplexShip()
    for a in inputs:
        c.update(a)   
        
    # answer_2 = solve(inputs)
    print(f"Part 2 answer: {sum(abs(a) for a in c.pos)}")
