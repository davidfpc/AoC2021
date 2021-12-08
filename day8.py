def read_input(file_name: str) -> [[str]]:
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return [i.split(" ") for i in lines]


def part1(input_value: [[str]]):
    counter = 0
    for rows in input_value:
        for i in rows[-4:]:
            length = len(i)
            # if digits 1 (len 2), 4 (len 4), 7 (len 3), or 8 (len 7)
            if length == 2 or length == 3 or length == 4 or length == 7:
                counter += 1
    return counter


def part2(input_value: [[str]]):
    sum_digits = 0
    for rows in input_value:
        number = 0
        for segment_number in rows[-4:]:
            length = len(segment_number)
            # if digit 1 (len 2)
            if length == 2:
                number = number * 10 + 1
            # if digit 7 (len 3)
            if length == 3:
                number = number * 10 + 7
            # if digit 4 (len 4)
            if length == 4:
                number = number * 10 + 4
            # if digit 2, 3, 5 (len 5)
            if length == 5:
                examples = rows[:-4]
                one = [a for a in examples if len(a) == 2][0]
                four = [a for a in examples if len(a) == 4][0]
                middle_part_of_five = [a for a in four if a not in one]
                # compare with 1 - if number contains same segments as 1, then it's a 3
                if len([a for a in segment_number if a in one]) == 2:
                    number = number * 10 + 3
                # compare with between 4 without the right part (a one) - if number contains same segments, then it's a 5
                elif len([a for a in segment_number if a in middle_part_of_five]) == 2:
                    number = number * 10 + 5
                else:
                    number = number * 10 + 2
            # if digit 0, 6, 9 (len 6)
            if length == 6:
                examples = rows[:-4]
                one = [a for a in examples if len(a) == 2][0]
                four = [a for a in examples if len(a) == 4][0]
                # check if it has the same segments as 1: if not, then it's a 6
                if len([a for a in segment_number if a in one]) == 1:
                    number = number * 10 + 6
                # compare with a 4 - if number contains same segments, then it's a 9
                elif len([a for a in segment_number if a in four]) == 4:
                    number = number * 10 + 9
                else:
                    number = number * 10
            # if digit  8 (len 7)
            if length == 7:
                number = number * 10 + 8
        sum_digits += number
    return sum_digits


if __name__ == "__main__":
    puzzle_input = read_input("day8.txt")
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
