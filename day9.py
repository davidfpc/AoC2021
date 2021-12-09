import numpy


def read_input(file_name: str) -> [str]:
    with open("inputFiles/" + file_name, "r") as file:
        return file.read().splitlines()


def part1(input_value: [str]):
    local_minimums = []
    for x in range(0, len(input_value[0])):
        for y in range(0, len(input_value)):
            if is_local_min(input_value, x, y):
                local_minimums.append(int(input_value[y][x]))
    return sum(local_minimums) + len(local_minimums)


def is_local_min(input_value: [str], x: int, y: int):
    if x > 0 and input_value[y][x] >= input_value[y][x - 1]:
        return False
    if x < (len(input_value[0]) - 1) and input_value[y][x] >= input_value[y][x + 1]:
        return False
    if y > 0 and input_value[y][x] >= input_value[y - 1][x]:
        return False
    if y < (len(input_value) - 1) and input_value[y][x] >= input_value[y + 1][x]:
        return False
    return True


def part2(input_value: [str]):
    basin_sizes = []
    visited_nodes = set()

    for x in range(0, len(input_value[0])):
        for y in range(0, len(input_value)):
            basin_size = get_basin_size(input_value, x, y, visited_nodes)
            basin_sizes.append(basin_size)

    basin_sizes.sort()
    return numpy.prod(basin_sizes[-3:])


def get_basin_size(input_value: [str], x: int, y: int, visited_sets: {(int, int)}):
    if x < 0 or x >= len(input_value[0]) or y < 0 or y >= len(input_value):
        return 0
    if (x, y) in visited_sets or input_value[y][x] == '9':
        return 0
    visited_sets.add((x, y))
    return 1 + get_basin_size(input_value, x - 1, y, visited_sets) + get_basin_size(input_value, x + 1, y, visited_sets) + get_basin_size(input_value, x, y - 1,
                                                                                                                                          visited_sets) + get_basin_size(
        input_value, x, y + 1, visited_sets)


if __name__ == "__main__":
    puzzle_input = read_input("day9.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
