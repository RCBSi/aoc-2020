from common import read_input

def get_addresses(addr, mask):
    addresses = []
    nbits = mask.count('X')
    base = [bin(i)[2:].zfill(nbits) for i in range(0, 2**nbits )]
    for b in base:
        it = iter(b)
        b_loc = "".join([a if m != 'X' else next(it) for a, m in zip(addr, mask)])
        addresses.append(int(b_loc, 2))
    return addresses

def solve_1(raw_in):
    mem = {}
    for line in raw_in:
        a,b = line.split(' = ')
        if a == 'mask':
            mask = b
        else:
            loc = int(a[4:-1])
            addr = f"{int(b):036b}"
            transformed = "".join(m if m != 'X' else b for m, b in zip(mask, addr))
            mem[loc] = transformed

    return sum(int(v, 2) for v in mem.values())


def solve_2(raw_in):
    mem = {}
    # ii = iter(raw_in)
    for line in raw_in:
        # line = next(ii)
        a, b = line.split(' = ')
        if a == 'mask':
            mask = b
            
        else:
            loc = int(a[4:-1])
            addr = f"{int(loc):036b}"
            addr_mod = "".join(m if m == "1" else a for a, m in zip(addr, mask))

            mask_addresses = get_addresses(addr_mod, mask)
            for a in mask_addresses:
                mem[a] = int(b)

    return sum(v for v in mem.values())



if __name__ == "__main__":
    raw_in = read_input("data/day_14.txt")

    answer_1 = solve_1(raw_in)
    answer_2 = solve_2(raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
