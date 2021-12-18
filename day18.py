# program to compute the time of execution of any python code
import copy
import time
from math import ceil


class Node:
    def __init__(self, left=None, right=None, parent=None):
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"Node(l= {self.left}, r= {self.right})"

    def __repr__(self) -> str:
        return self.__str__()


class NodeValue:
    def __init__(self, value: int, parent=None):
        self.parent = parent
        self.value = value

    def __str__(self) -> str:
        return f"[value = {self.value}]"

    def __repr__(self) -> str:
        return self.__str__()


def read_input(file_name: str):
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return [i for i, _ in [parse_node(i) for i in lines]]


def parse_node(input_value: str) -> (Node, str):
    node = Node()
    if input_value[1] == '[':
        node.left, input_value = parse_node(input_value[1:])
        node.left.parent = node
    else:
        node.left = NodeValue(int(input_value[1]), node)
        input_value = input_value[2:]
    input_value = input_value[1:]
    if input_value[0] == '[':
        node.right, input_value = parse_node(input_value[0:])
        node.right.parent = node
    else:
        node.right = NodeValue(int(input_value[0]), node)
        input_value = input_value[1:]
    return node, input_value[1:]


def reduce(snailfish: Node):
    reduced = True
    while reduced:
        reduced = try_explode(snailfish)
        if reduced:
            continue
        reduced = try_split(snailfish)
    return snailfish


def try_explode(elem: Node, depth: int = 1) -> bool:
    for value, right_side in [(elem.left, False), (elem.right, True)]:
        if type(value) is Node:
            if depth == 4:
                # Explode
                # right
                if right_side:
                    tmp_value = value
                    tmp_parent = value.parent
                    while tmp_parent is not None and tmp_parent.right == tmp_value:
                        tmp_value = tmp_parent
                        tmp_parent = tmp_parent.parent
                    if tmp_parent is not None:
                        add_to_most_at_side(tmp_parent.right, value.right, False)
                else:
                    add_to_most_at_side(value.parent.right, value.right, False)
                # left
                if right_side:
                    add_to_most_at_side(value.parent.left, value.left, True)
                else:
                    tmp_value = value
                    tmp_parent = value.parent
                    while tmp_parent is not None and tmp_parent.left == tmp_value:
                        tmp_value = tmp_parent
                        tmp_parent = tmp_parent.parent
                    if tmp_parent is not None:
                        add_to_most_at_side(tmp_parent.left, value.left, True)
                if value.parent.left == value:
                    value.parent.left = NodeValue(0, value.parent)
                else:
                    value.parent.right = NodeValue(0, value.parent)
                return True
            else:
                result = try_explode(value, depth + 1)
                if result:
                    return True


def add_to_most_at_side(elem, value_to_add: NodeValue, right_side: bool):
    if type(elem) is NodeValue:
        elem.value = elem.value + value_to_add.value
    else:
        if right_side:
            value = elem.right
        else:
            value = elem.left

        if type(value) is NodeValue:
            value.value += value_to_add.value
        else:
            add_to_most_at_side(value, value_to_add, right_side)


def try_split(elem) -> bool:
    for value in [elem.left, elem.right]:
        if type(value) is Node:
            result = try_split(value)
            if result:
                return True
        else:
            if value.value >= 10:
                # split
                new_value = value.value / 2
                new_node = Node(parent=elem)
                new_node.left = NodeValue(int(new_value), new_node)
                new_node.right = NodeValue(ceil(new_value), new_node)
                if value.parent.right == value:
                    elem.right = new_node
                else:
                    elem.left = new_node
                return True
    return False


def calc_magnitude(elem) -> int:
    if type(elem) == NodeValue:
        return elem.value
    return calc_magnitude(elem.left) * 3 + calc_magnitude(elem.right) * 2


def part1(input_value) -> int:
    snail_fish_sum = input_value[0]
    for i in range(1, len(input_value)):
        new_node = Node(snail_fish_sum, input_value[i])
        snail_fish_sum.parent = new_node
        input_value[i].parent = new_node
        snail_fish_sum = reduce(new_node)

    return calc_magnitude(snail_fish_sum)


def part2(input_value) -> int:
    results = []
    for i in range(len(input_value) - 1):
        for a in range(i + 1, len(input_value)):
            if i == a:
                continue
            value_i = copy.deepcopy(input_value[i])
            value_a = copy.deepcopy(input_value[a])
            new_node = Node(value_i, value_a)
            value_i.parent = new_node
            value_a.parent = new_node
            result = calc_magnitude(reduce(new_node))
            results.append(result)

    return max(results)


if __name__ == "__main__":
    start = time.time()
    puzzle_input = read_input("day18.txt")
    print(f"Part 2: {part2(puzzle_input)}")
    print(f"Part 1: {part1(puzzle_input)}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
