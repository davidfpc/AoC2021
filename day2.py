class Position:
    def __init__(self):
        self.depth = 0
        self.x_pos = 0
        self.aim = 0

    def __str__(self) -> str:
        return f"Position(x_pos:{self.x_pos}, depth:{self.depth}, aim:{self.aim})"

    def __repr__(self) -> str:
        return self.__str__()

    def forward(self, value: int):
        self.x_pos = self.x_pos + value
        self.depth = self.depth + (self.aim * value)

    def down(self, value: int):
        self.aim = self.aim + value

    def up(self, value: int):
        self.aim = self.aim - value


class Instruction:
    def __init__(self, instruction: str):
        tmp = instruction.split()
        self.instruction = tmp[0]
        self.value = int(tmp[1])

    def __str__(self) -> str:
        return f"Instruction({self.instruction} -> {self.value})"

    def __repr__(self) -> str:
        return self.__str__()

    def process_position(self, position: Position):
        if self.instruction == "forward":
            position.forward(self.value)
        elif self.instruction == "down":
            position.down(self.value)
        else:
            position.up(self.value)


def read_input(file_name: str):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return [Instruction(i) for i in lines]


def part1(input_value: [Instruction]):
    x_pos = 0
    depth = 0
    for instruction in input_value:
        if instruction.instruction == "forward":
            x_pos = x_pos + instruction.value
        elif instruction.instruction == "down":
            depth = depth + instruction.value
        else:
            depth = depth - instruction.value
    print(f"Final position: {x_pos} -> {depth}")
    return x_pos * depth


def part2(input_value: [Instruction]):
    position = Position()
    for instruction in input_value:
        instruction.process_position(position)
    print(f"Final position: {position}")
    return position.x_pos * position.depth


if __name__ == "__main__":
    puzzle_input = read_input("day2.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))
