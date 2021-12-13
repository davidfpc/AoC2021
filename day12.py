# program to compute the time
# of execution of any python code
import copy
import time


def read_input(file_name: str) -> {str: {str}}:
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        input_map = {}
        # create unidirectional graph
        for i in lines:
            source, dest = i.split('-')
            if source in input_map.keys():
                input_map.get(source).add(dest)
            else:
                input_map[source] = {dest}

        for i in list(input_map.keys()):
            for z in input_map.get(i):
                if z in input_map.keys():
                    input_map.get(z).add(i)
                else:
                    input_map[z] = {i}

        return input_map


def part1(input_value: {str: {str}}, current_path: [str]):
    current_node = current_path[-1]

    if current_node == 'end':
        return 1
    if current_node not in input_value.keys():
        return 0

    path_sum = 0
    for i in input_value[current_node]:
        if i in current_path and not all(char.isupper() for char in i):
            continue
        else:
            path_sum += part1(input_value, current_path[:] + [i])
    return path_sum


def part2(input_value: {str: {str}}, current_path: [str], visited_small: bool = False):
    current_node = current_path[-1]
    if current_node == 'end':
        return 1
    if current_node not in input_value.keys():
        return 0

    path_sum = 0
    for i in input_value[current_node]:
        if i in current_path and not all(char.isupper() for char in i):
            if i != 'start' and not visited_small:
                # we can have the same element twice, so try both options
                path_sum += part2(input_value, current_path[:] + [i], True)
        else:
            path_sum += part2(input_value, current_path[:] + [i], visited_small)
    return path_sum


if __name__ == "__main__":
    puzzle_input = read_input("day12.txt")
    start = time.time()
    print(f"Part 1: {part1(copy.deepcopy(puzzle_input), ['start'])}")
    print(f"Part 2: {part2(copy.deepcopy(puzzle_input), ['start'])}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
