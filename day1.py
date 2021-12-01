import numpy as np


def read_input(file_name):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return [int(i, base=16) for i in lines]


def part1(input_value):
    prev_value = input_value[0]
    counter = 0
    for i in input_value[1:]:
        if int(i) > prev_value:
            counter = counter + 1
        prev_value = i
    return counter


def part2(input_value):
    windowed_input = list(map(lambda x: sum(x), np.lib.stride_tricks.sliding_window_view(input_value, 3)))
    return part1(windowed_input)


if __name__ == "__main__":
    puzzle_input = read_input("day1.txt")
    print(part1(puzzle_input))
    print(part2(puzzle_input))
