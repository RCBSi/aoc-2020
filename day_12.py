from common import read_input

DIRS = {"N": 1j, "E": 1, "S": -1j, "W": -1}
ROTS = {"R": -1, "L": 1}

def solve(actions, wpt, pos_moves):
    pos = complex(0, 0)
    for a in actions:
        cmd, value = a[0], int(a[1:])
        if cmd in "NSEW":
            if pos_moves:
                pos += value * DIRS[cmd]
            else:
                wpt += value * DIRS[cmd]
        elif cmd in "LR":
            wpt = (1j ** (ROTS[cmd] * (value / 90))) * wpt
        elif cmd == "F":
            pos += value * wpt
    print(f"Manhattan distance: {int(abs(pos.real) + abs(pos.imag))}")

if __name__ == "__main__":
    actions = read_input("data/day_12.txt")

    solve(actions, wpt=complex(1, 0), pos_moves=True)
    solve(actions, wpt=complex(10, 1), pos_moves=False)
