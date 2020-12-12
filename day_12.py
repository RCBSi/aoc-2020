from common import read_input

DIRS = {
    "N": complex(0, 1),
    "E": complex(1, 0),
    "S": complex(0, -1),
    "W": complex(-1, 0),
}

ROTS = {"R": -1, "L": 1}


def _rotate_point(point, cmd, value):
    v = ROTS[cmd] * (value / 90)
    return (1j ** v) * point


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
            wpt = _rotate_point(wpt, cmd, value)
        elif cmd == "F":
            pos += value * wpt

    print(f"Manhattan distance: {int(abs(pos.real) + abs(pos.imag))}")


if __name__ == "__main__":
    actions = read_input("data/day_12.txt")

    solve(actions, wpt=complex(1, 0), pos_moves=True)
    solve(actions, wpt=complex(10, 1), pos_moves=False)
