# program to compute the time
# of execution of any python code
import time


class Coord:

    def __init__(self, x: int, y: int):
        self.x_pos = x
        self.y_pos = y

    @classmethod
    def parse(cls, input_value: str):
        x, y = input_value.split(',')
        return cls(int(x), int(y))

    def __str__(self) -> str:
        return f"(x_pos:{self.x_pos}, y_pos:{self.y_pos})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other):
        return self.x_pos == other.x_pos and self.y_pos == other.y_pos

    def __hash__(self):
        return hash((self.x_pos, self.y_pos))


class Instruction:
    def __init__(self, instruction: str):
        axis, value = instruction.split('=')
        self.axis = axis[-1]
        self.value = int(value)

    def __str__(self) -> str:
        return f"Instruction({self.axis} -> {self.value})"

    def __repr__(self) -> str:
        return self.__str__()


def read_input(file_name: str) -> ([Coord], [Instruction]):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return [Coord.parse(i) for i in lines[:lines.index('')]], [Instruction(i) for i in lines[lines.index('') + 1:]]


def part1(input_value: ([Coord], [Instruction])):
    instruction: Instruction = input_value[1][0]
    result = process_fold(instruction, input_value[0])
    return len(result)


def process_fold(instruction: Instruction, coords: [Coord]) -> [Coord]:
    new_coords = set()
    for coord in coords:
        if instruction.axis == 'x' and coord.x_pos > instruction.value:
            new_coords.add(Coord(instruction.value - abs(instruction.value - coord.x_pos), coord.y_pos))
        elif instruction.axis == 'y' and coord.y_pos > instruction.value:
            new_coords.add(Coord(coord.x_pos, instruction.value - abs(instruction.value - coord.y_pos)))
        else:
            new_coords.add(coord)
    return new_coords


def part2(input_value: ([Coord], [Instruction])):
    result = input_value[0]
    for i in input_value[1]:
        result = process_fold(i, result)

    max_x = max([i.x_pos for i in result])
    max_y = max([i.y_pos for i in result])
    for y in range(0, max_y + 2):
        for x in range(0, max_x + 2):
            if Coord(x, y) in result:
                print("#", end="")
            else:
                print(" ", end="")
        print("")


if __name__ == "__main__":
    puzzle_input = read_input("day13.txt")
    start = time.time()
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
