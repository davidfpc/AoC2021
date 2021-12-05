def read_input(file_name: str):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return lines


def part1(input_value: [str]):
    position_map = {}
    for i in input_value:
        cords = i.split(" -> ")
        start_cords = [int(cord) for cord in cords[0].split(",")]
        end_cords = [int(cord) for cord in cords[1].split(",")]
        if start_cords[0] == end_cords[0]:
            # Vertical alignment
            minimum = min(start_cords[1], end_cords[1])
            maximum = max(start_cords[1], end_cords[1])
            while minimum <= maximum:
                set_position((start_cords[0], minimum), position_map)
                minimum += 1
        elif start_cords[1] == end_cords[1]:
            # Horizontal alignment
            minimum = min(start_cords[0], end_cords[0])
            maximum = max(start_cords[0], end_cords[0])
            while minimum <= maximum:
                set_position((minimum, start_cords[1]), position_map)
                minimum += 1
    return len([i for i in position_map.values() if i > 1])


def part2(input_value: [str]):
    position_map = {}
    for i in input_value:
        cords = i.split(" -> ")
        start_cords = [int(cord) for cord in cords[0].split(",")]
        end_cords = [int(cord) for cord in cords[1].split(",")]
        if start_cords[0] == end_cords[0]:
            # Vertical alignment
            minimum = min(start_cords[1], end_cords[1])
            maximum = max(start_cords[1], end_cords[1])
            while minimum <= maximum:
                set_position((start_cords[0], minimum), position_map)
                minimum += 1
        elif start_cords[1] == end_cords[1]:
            # Horizontal alignment
            minimum = min(start_cords[0], end_cords[0])
            maximum = max(start_cords[0], end_cords[0])
            while minimum <= maximum:
                set_position((minimum, start_cords[1]), position_map)
                minimum += 1
        else:
            # diagonal alignment
            start_x = start_cords[0]
            end_x = end_cords[0]
            start_y = start_cords[1]
            end_y = end_cords[1]
            # 9,7 -> 7,9
            set_position((start_x, start_y), position_map)
            while start_x != end_x and start_y != end_y:
                if start_x > end_x:
                    start_x -= 1
                elif start_x < end_x:
                    start_x += 1
                if start_y > end_y:
                    start_y -= 1
                elif start_y < end_y:
                    start_y += 1
                set_position((start_x, start_y), position_map)
    return len([i for i in position_map.values() if i > 1])


def set_position(position, position_map):
    if position in position_map:
        position_map[position] += 1
    else:
        position_map[position] = 1


if __name__ == "__main__":
    puzzle_input = read_input("day5.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
