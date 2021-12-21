# program to compute the time of execution of any python code
import time


def read_input(file_name: str) -> (int, int):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return int(lines[0].removeprefix("Player 1 starting position: ")), int(lines[1].removeprefix("Player 2 starting position: "))


def part1(input_value: (int, int)) -> int:
    players_pos = [input_value[0], input_value[1]]
    player_score = [0, 0]
    rolls = 0

    while True:
        for i in range(2):
            players_pos[i] = (players_pos[i] + sum([get_deterministic_dice_value() for _ in range(3)])) % 10
            rolls += 3
            if players_pos[i] == 0:
                players_pos[i] = 10
            player_score[i] += players_pos[i]
            if player_score[i] >= 1000:
                return player_score[(i + 1) % 2] * rolls


dice = 0


def get_deterministic_dice_value() -> int:
    global dice
    dice += 1
    if dice == 101:
        dice = 1
    return dice


cache: {((int, int), (int, int)): (int, int)} = {}
die_options = [sum([i, j, k]) for i in range(1, 4) for j in range(1, 4) for k in range(1, 4)]
MAX_SCORE: int = 21


def part2(input_value: (int, int)) -> int:
    p1_pos, p2_pos = input_value
    p1_win_count, p2_win_count = potatoes(p1_pos, p2_pos, 0, 0)
    return max(p1_win_count, p2_win_count)


def potatoes(p1_pos: int, p2_pos: int, p1_score: int, p2_score: int) -> (int, int):
    p1_wins = p2_wins = 0
    for i in die_options:
        tmp_p1_pos = (p1_pos + i) % 10
        if tmp_p1_pos == 0:
            tmp_p1_pos = 10
        tmp_p1_score = p1_score + tmp_p1_pos
        if tmp_p1_score >= MAX_SCORE:
            p1_wins += 1
        else:
            for j in die_options:
                tmp_p2_pos = (p2_pos + j) % 10
                if tmp_p2_pos == 0:
                    tmp_p2_pos = 10
                tmp_p2_score = p2_score + tmp_p2_pos
                if tmp_p2_score >= MAX_SCORE:
                    p2_wins += 1
                else:
                    if ((tmp_p1_pos, tmp_p1_score), (tmp_p2_pos, tmp_p2_score)) in cache:
                        tmp_p1_wins, tmp_p2_wins = cache[((tmp_p1_pos, tmp_p1_score), (tmp_p2_pos, tmp_p2_score))]
                    else:
                        tmp_p1_wins, tmp_p2_wins = potatoes(tmp_p1_pos, tmp_p2_pos, tmp_p1_score, tmp_p2_score)
                    p1_wins += tmp_p1_wins
                    p2_wins += tmp_p2_wins
    cache[((p1_pos, p1_score), (p2_pos, p2_score))] = (p1_wins, p2_wins)
    return p1_wins, p2_wins


if __name__ == "__main__":
    start = time.time()
    puzzle_input = read_input("day21.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
