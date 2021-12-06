def read_input(file_name: str) -> [int]:
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()[0].split(",")
        return [int(i) for i in lines]


def part1(input_value: [int], max_days: int):
    i = 0
    while i < max_days:
        for index in range(len(input_value)):
            fish = input_value[index]
            if fish == 0:
                input_value[index] = 6
                input_value.append(8)
            else:
                input_value[index] = input_value[index] - 1
        i += 1
    return len(input_value)


def part2(input_value: [int], max_days: int):
    number_of_fish = [0] * 9
    for fish in input_value:
        number_of_fish[fish] = number_of_fish[fish] + 1

    i = 0
    while i < max_days:
        new_fish = number_of_fish[0]
        for index in range(1, 9):
            number_of_fish[index - 1] = number_of_fish[index]
        number_of_fish[8] = new_fish
        number_of_fish[6] = number_of_fish[6] + new_fish
        i += 1
    return sum(number_of_fish)


if __name__ == "__main__":
    puzzle_input = read_input("day6.txt")
    print(f"Part 1: {part1(puzzle_input[:], 80)}")
    print(f"Part 2: {part2(puzzle_input, 256)}")
