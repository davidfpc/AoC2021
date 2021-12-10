def read_input(file_name: str) -> [str]:
    with open("inputFiles/" + file_name, "r") as file:
        return file.read().splitlines()


open_chunk = {'(': ')', '[': ']', '{': '}', '<': '>'}
close_chunk = {')': '(', ']': '[', '}': '{', '>': '<'}
error_score_board = {')': 3, ']': 57, '}': 1197, '>': 25137}
fix_score_board = {')': 1, ']': 2, '}': 3, '>': 4}


def part1(input_value: [str]):
    score = 0
    for row in input_value:
        invalid_value = is_row_valid(row)
        if invalid_value is not None:
            score += error_score_board.get(invalid_value)
    return score


def is_row_valid(row: str) -> chr:
    stack = []
    for i in row:
        # Open chunk
        if i in open_chunk.keys():
            stack.append(i)
        # Close chunk
        if i in close_chunk.keys():
            # no chunk to close
            if len(stack) == 0:
                return i
            else:
                open_char = close_chunk.get(i)
                current_chunk = stack.pop()
                # invalid chunk
                if open_char != current_chunk:
                    return i


def part2(input_value: [str]):
    filtered_input_value = [row for row in input_value if is_row_valid(row) is None]
    score = []
    for row in filtered_input_value:
        stack = []
        for i in row:
            # Open chunk
            if i in open_chunk.keys():
                stack.append(i)
            # Close chunk
            elif i in close_chunk.keys():
                stack.pop()
        row_score = 0
        stack.reverse()
        for i in stack:
            row_score = (5 * row_score) + fix_score_board.get(open_chunk.get(i))
        score.append(row_score)
    score.sort()
    return score[int(len(score) / 2)]


if __name__ == "__main__":
    puzzle_input = read_input("day10.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
