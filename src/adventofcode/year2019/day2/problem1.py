class IntcodeProgram:
    def __init__(self, initial_state):
        self.state = initial_state
        self.current_position = 0

    def handle_opcode_1(self):
        self.state[self.state[self.current_position + 3]] = (
            self.state[self.state[self.current_position + 1]]
            + self.state[self.state[self.current_position + 2]]
        )
        return None

    def handle_opcode_2(self):
        self.state[self.state[self.current_position + 3]] = (
                self.state[self.state[self.current_position + 1]]
                * self.state[self.state[self.current_position + 2]]
        )
        return None

    def handle_opcode_99(self):
        return self.state[0]

    def process_position(self):
        return {
            1: self.handle_opcode_1,
            2: self.handle_opcode_2,
            99: self.handle_opcode_99,
        }.get(self.state[self.current_position])()

    def run(self):

        exit_code = None
        while not exit_code:
            print(self.state)
            exit_code = self.process_position()
            self.current_position += 4
        return exit_code


if __name__ == "__main__":
    with open("input.txt") as f:
        numbers = list(map(int, f.read().split(",")))

    numbers[1] = 12
    numbers[2] = 2

    result = IntcodeProgram(numbers).run()

    print(result)
