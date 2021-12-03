def read_input(file_name: str):
    with open("inputFiles/" + file_name, "r") as file:
        return file.read().splitlines()


def part1(input_value: [[int]]):
    gamma = 0
    epsilon = 0
    for i in range(len(input_value[0])):
        values = [int(report[i]) for report in input_value]
        gamma = gamma * 10 + round(sum(values) / len(values))
        epsilon = epsilon * 10 + round(1 - (sum(values) / len(values)))
    gamma = int(str(gamma), 2)
    epsilon = int(str(epsilon), 2)
    print(f"gamma: {gamma}, epsilon: {epsilon}")
    return gamma * epsilon


def part2(input_value: [str]):
    oxygen = input_value.copy()
    co2 = input_value.copy()
    for i in range(len(input_value[0])):
        if len(oxygen) > 1:
            values = [int(report[i]) for report in oxygen]
            most_significant_value = 1 if sum(values) / len(values) >= 0.5 else 0
            oxygen = [report for report in oxygen if int(report[i]) == most_significant_value]
        if len(co2) > 1:
            values = [int(report[i]) for report in co2]
            least_significant_value = round(1 - sum(values) / len(values))
            co2 = [report for report in co2 if int(report[i]) == least_significant_value]
    oxygen = int(oxygen[0], 2)
    co2 = int(co2[0], 2)
    print(f"oxygen: {oxygen}, co2: {co2}")
    return oxygen * co2


if __name__ == "__main__":
    puzzle_input = read_input("day3.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
