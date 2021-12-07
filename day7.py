def read_input(file_name: str) -> [int]:
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()[0].split(",")
        return [int(i) for i in lines]


def part1(input_value: [int]):
    min_fuel = -1
    for i in range(max(input_value)):
        fuel = 0
        for fish in input_value:
            fuel += abs(i - fish)
        if min_fuel == -1 or fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


def part2(input_value: [int]):
    min_fuel = -1
    for i in range(max(input_value)):
        fuel = 0
        for fish in input_value:
            fuel += sum(range(1, abs(i - fish) + 1))
        if min_fuel == -1 or fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


if __name__ == "__main__":
    puzzle_input = read_input("day7.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
