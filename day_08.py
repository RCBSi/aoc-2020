from common import read_input


def parse_instruction(s):
    a, b = s.split(" ")
    return a, int(b)


def get_program():
    return [parse_instruction(x) for x in read_input("data/day_08.txt")]


class Computer:
    def __init__(self):
        self.reset()

    def load_program(self, s):
        self.program = s

    def reset(self):
        self.pointer = 0
        self.acc = 0
        self.i = 0
        self.error_loop = False
        self.finished_successfully = False
        self.previous_states = set()

    def step(self):
        code, value = self.program[self.pointer]

        # Halt execution if state is not valid
        if self.finished_successfully == True:
            print("Already finished")
            return

        if self.error_loop == True:
            print("Cannot run in a loop state")
            return

        # Determine next state
        if code == "nop":
            pointer_next = self.pointer + 1
            acc_next = self.acc
        if code == "acc":
            pointer_next = self.pointer + 1
            acc_next = self.acc + value
        if code == "jmp":
            pointer_next = self.pointer + value
            acc_next = self.acc

        next_state = (pointer_next, acc_next)

        # Update state
        if pointer_next >= len(self.program):
            self.finished_successfully = True
            # print("Finished running successfully")
            return

        if pointer_next not in self.previous_states:
            self.pointer, self.acc = next_state
            self.previous_states.add(pointer_next)
            self.i += 1
            return
        else:
            self.error_loop = True
            # print(f"Loop found on iteration {self.i}, aborting")
            return

    def run(self):
        while (not self.error_loop) & (not self.finished_successfully):
            self.step()

    def __repr__(self):
        s = f"Computer with state:\n"
        s += f"  i {self.i}\n"
        s += f"  pointer {self.pointer}\n"
        s += f"  acc {str(self.acc)}\n"
        s += f"  error_loop {self.error_loop}\n"
        s += f"  finished_succesfully {self.finished_successfully}\n"
        s += f"Number of states visited: {len(self.previous_states)}\n"
        return s


def generate_possible_variations(program):
    nop_idxes = [i for i, c in enumerate(program) if c[0] == "nop"]
    jmp_idxes = [i for i, c in enumerate(program) if c[0] == "jmp"]

    for ni in nop_idxes:
        p = program.copy()
        p[ni] = ("jmp", p[ni][1])
        yield p

    for ji in jmp_idxes:
        p = program.copy()
        p[ji] = ("nop", p[ji][1])
        yield p


if __name__ == "__main__":
    program = get_program()

    computer = Computer()
    computer.load_program(program)

    # Part 1
    computer.run()
    print(f"Part 1 answer: {computer.acc}")

    # Part 2
    code_variations = generate_possible_variations(program)

    while True:
        code_trial = next(code_variations)

        computer.reset()
        computer.load_program(code_trial)
        computer.run()

        if computer.finished_successfully:
            break

    print(f"Part 2 answer: {computer.acc}")
