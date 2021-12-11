import copy

GENERATIONS = 100


def read_input(file_name: str) -> [[int]]:
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return [[(int(i), False) for i in line] for line in lines]


def part1(input_value: [[int]]):
    flash_count = 0
    for gen in range(GENERATIONS):
        # Increment energy
        flash_count += process_generation(input_value)
    return flash_count


def process_generation(input_value) -> int:
    flash_count = 0
    # Increment energy
    for x in range(len(input_value[0])):
        for y in range(len(input_value)):
            input_value[y][x] = (input_value[y][x][0] + 1, False)
    # Check for flashes
    for x in range(len(input_value[0])):
        for y in range(len(input_value)):
            if input_value[y][x][0] > 9:
                # Houston, we have a Flash!
                flash_count += flash(x, y, input_value)
    for x in range(len(input_value[0])):
        for y in range(len(input_value)):
            if input_value[y][x][1]:
                input_value[y][x] = (0, False)
    return flash_count


def flash(x: int, y: int, input_value) -> int:
    input_value[y][x] = (input_value[y][x][1], True)
    flash_count = 1
    flash_count += increase_energy(x - 1, y - 1, input_value)
    flash_count += increase_energy(x - 1, y, input_value)
    flash_count += increase_energy(x - 1, y + 1, input_value)
    flash_count += increase_energy(x, y - 1, input_value)
    flash_count += increase_energy(x, y + 1, input_value)
    flash_count += increase_energy(x + 1, y - 1, input_value)
    flash_count += increase_energy(x + 1, y, input_value)
    flash_count += increase_energy(x + 1, y + 1, input_value)
    return flash_count


def increase_energy(x: int, y: int, input_value) -> int:
    if x >= len(input_value[0]) or x < 0 or y >= len(input_value) or y < 0:
        return 0
    # increase energy
    input_value[y][x] = (input_value[y][x][0] + 1, input_value[y][x][1])
    if input_value[y][x][0] > 9:
        return flash(x, y, input_value)
    return 0


def part2(input_value: [[int]]):
    generation = 0
    while not check_sync_flash(input_value):
        # Increment energy
        process_generation(input_value)
        generation += 1
    return generation


def check_sync_flash(input_value: [[int]]) -> bool:
    for x in range(len(input_value[0])):
        for y in range(len(input_value)):
            if input_value[y][x][0] != 0:
                return False
    return True


if __name__ == "__main__":
    puzzle_input = read_input("day11.txt")
    print(f"Part 1: {part1(copy.deepcopy(puzzle_input))}")
    print(f"Part 2: {part2(copy.deepcopy(puzzle_input))}")
