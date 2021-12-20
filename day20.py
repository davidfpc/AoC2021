# program to compute the time of execution of any python code
import time


def read_input(file_name: str) -> (str, [str]):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return lines[0], lines[2:]


def enhance_image(algorithm: str, image: [str], infinite: str) -> [str]:
    new_image = []
    for y in range(-1, len(image) + 1):
        new_row = ""
        for x in range(-1, len(image[0]) + 1):
            algorithm_index = ""
            for x_delta, y_delta in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                algorithm_index += get_pos(image, x + x_delta, y + y_delta, infinite)
            new_row += algorithm[int(algorithm_index, 2)]
        new_image.append(new_row)
    return new_image


def get_pos(image: [str], x: int, y: int, default: str) -> str:
    char = default
    if 0 <= x < len(image[0]) and 0 <= y < len(image):
        char = image[y][x]
    if char == '#':
        return '1'
    return '0'


def print_image(image: [str]):
    for y in range(-2, len(image) + 2):
        for x in range(-2, len(image[0]) + 2):
            if 0 <= x < len(image[0]) and 0 <= y < len(image):
                if image[y][x] == '#':
                    print('#', end='')
                    continue
            print('.', end='')
        print()


def part1(input_value: (str, [str])) -> int:
    algorithm, image = input_value

    image = enhance_image(algorithm, image, '.')
    image = enhance_image(algorithm, image, algorithm[0])

    count = sum([len(i.replace('.', '')) for i in image])
    return count


def part2(input_value) -> int:
    algorithm, image = input_value
    default = '.'
    default2 = algorithm[0]
    for i in range(50):
        image = enhance_image(algorithm, image, default)
        tmp = default
        default = default2
        default2 = tmp
    count = sum([len(i.replace('.', '')) for i in image])
    # print_image(image)
    return count


if __name__ == "__main__":
    start = time.time()
    puzzle_input = read_input("day20.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
