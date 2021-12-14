# program to compute the time
# of execution of any python code
import time
from collections import Counter


def read_input(file_name: str) -> (str, {str: str}):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        rule = {}
        for i in lines[2:]:
            pair, element = i.split(" -> ")
            rule[pair] = element
        return lines[0], rule


def part1(input_value: (str, {str: str})) -> int:
    template, rules = input_value

    for i in range(10):
        tmp_template = ""
        for pos in range(len(template) - 1):
            tmp_template += template[pos]
            tmp_template += rules[template[pos] + template[pos + 1]]
        tmp_template += template[len(template) - 1]
        template = tmp_template

    frequency = [value for value in Counter(template).values()]
    min_freq = min(frequency)
    max_freq = max(frequency)
    return max_freq - min_freq


def add_to_dict(dictionary, key, value):
    if key in dictionary.keys():
        dictionary[key] = dictionary[key] + value
    else:
        dictionary[key] = value


def part2(input_value: (str, {str: str})) -> int:
    template, rules = input_value
    pair_count: {str: int} = {}
    # prepare dict
    for pos in range(len(template) - 1):
        pair = template[pos] + template[pos + 1]
        add_to_dict(pair_count, pair, 1)

    for i in range(40):
        tmp_pair_count = {}
        for pair, count in pair_count.items():
            new_letter = rules[pair]
            add_to_dict(tmp_pair_count, pair[0] + new_letter, count)
            add_to_dict(tmp_pair_count, new_letter + pair[1], count)
        pair_count = tmp_pair_count

    letter_count: {str: int} = {}
    for pair, count in pair_count.items():
        add_to_dict(letter_count, pair[0], count)
    add_to_dict(letter_count, template[-1], 1)

    min_freq = min(letter_count.values())
    max_freq = max(letter_count.values())
    return max_freq - min_freq


if __name__ == "__main__":
    puzzle_input = read_input("day14.txt")
    start = time.time()
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
