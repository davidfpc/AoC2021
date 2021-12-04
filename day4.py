import copy


def read_input(file_name: str):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        draw_numbers = [int(i) for i in lines[0].split(',')]
        boards = []
        board = []
        for i in lines[2:]:
            if i == '':
                boards.append(board)
                board = []
            else:
                board.append([int(elem) for elem in i.split()])
        boards.append(board)
        return draw_numbers, boards


def part1(input_value: ([int], [[int]])):
    draw_numbers, boards = input_value
    boards = copy.deepcopy(boards)
    won = False
    for number in draw_numbers:
        for board in boards:
            for row in board:
                if number in row:
                    for i in range(len(row)):
                        if row[i] == number:
                            row[i] = -1
                if all(elem == -1 for elem in row):
                    won = True
            for i in range(len(board[0])):
                column_elems = [row[i] for row in board]
                if all(elem == -1 for elem in column_elems):
                    won = True
            if won:
                return winner_sum(number, board)


def winner_sum(number: int, board: [[int]]):
    filtered_board = copy.deepcopy(board)
    for row in range(len(filtered_board)):
        filtered_board[row] = list(filter((-1).__ne__, filtered_board[row]))
    print(f"number:{number}, board: {filtered_board}")
    elem_sum = sum([sum(i) for i in filtered_board])
    return elem_sum * number


def part2(input_value: ([int], [[int]])):
    draw_numbers, boards = input_value
    boards = copy.deepcopy(boards)
    won = False
    for number in draw_numbers:
        boards = [i for i in boards if len(i) > 0]
        for board_index in range(len(boards)):
            board = boards[board_index]
            for row in board:
                if number in row:
                    for i in range(len(row)):
                        if row[i] == number:
                            row[i] = -1
                if all(elem == -1 for elem in row):
                    won = True
            for i in range(len(board[0])):
                column_elems = [row[i] for row in board]
                if all(elem == -1 for elem in column_elems):
                    won = True
            if won:
                if len(boards) == 1:
                    return winner_sum(number, board)
                else:
                    boards[board_index] = []
                    won = False


if __name__ == "__main__":
    puzzle_input = read_input("day4.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
