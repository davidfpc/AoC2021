# program to compute the time of execution of any python code
import time


def read_input(file_name: str) -> ((int, int), (int, int)):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        tmp = lines[0].split(", y=")
        x = [int(i) for i in tmp[0].removeprefix("target area: x=").split("..")]
        y = [int(i) for i in tmp[1].split("..")]
        return x, y


def part1(input_value: ((int, int), (int, int))) -> int:
    _, max_y = process(input_value)
    return max_y


def process(input_value: ((int, int), (int, int))) -> (int, int):
    target_x, target_y = input_value
    max_y = 0
    count = 0
    for v_x in range(1, target_x[1] + 1):
        for v_y in range(target_y[0], (target_x[1] + 1)):
            x = y = 0
            tmp_v_x = v_x
            tmp_v_y = v_y
            tmp_max = 0
            while True:
                x += tmp_v_x
                y += tmp_v_y
                if tmp_v_x > 0:
                    tmp_v_x -= 1
                elif tmp_v_x < 0:
                    tmp_v_x += 1
                tmp_v_y -= 1
                if y > tmp_max:
                    tmp_max = y

                if x > target_x[1] or y < target_y[0]:
                    # missed target
                    break
                if target_x[0] <= x <= target_x[1] and target_y[0] <= y <= target_y[1]:
                    count += 1
                    # target
                    if tmp_max > max_y:
                        max_y = tmp_max
                    break
    return count, max_y


def part2(input_value: ((int, int), (int, int))) -> int:
    count, _ = process(input_value)
    return count


if __name__ == "__main__":
    start = time.time()
    puzzle_input = read_input("day17.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
