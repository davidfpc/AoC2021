# program to compute the time of execution of any python code
import time
from queue import Queue

import numpy as np


class Packet(object):
    def __init__(self, input_value: Queue, version: int, packet_type: int):
        self.input_value = input_value
        self.version = version
        self.packet_type = packet_type
        self.children = []

    def parse_packet(self):
        pass

    def execute(self) -> int:
        pass

    @staticmethod
    def parse(input_value: Queue):
        version = int(get_bits(input_value, 3), 2)
        packet_type = int(get_bits(input_value, 3), 2)

        if packet_type == 4:
            packet = LiteralValuePacket(input_value, version, packet_type)
        else:
            packet = OperatorPacket(input_value, version, packet_type)

        packet.parse()
        return packet

    def __repr__(self) -> str:
        return self.__str__()


class LiteralValuePacket(Packet):
    def __init__(self, input_value: Queue, version: int, packet_type: int):
        Packet.__init__(self, input_value, version, packet_type)
        self.value = ""

    def parse(self):
        loop = True
        while loop:
            if get_bits(self.input_value, 1) == "0":
                loop = False
            self.value += get_bits(self.input_value, 4)
        self.value = int(self.value, 2)

    def execute(self):
        return self.value

    def __str__(self) -> str:
        return f"Packet(v={self.version},t={self.packet_type},v={self.value})"


class OperatorPacket(Packet):
    def __init__(self, input_value: Queue, version: int, packet_type: int):
        Packet.__init__(self, input_value, version, packet_type)

    def parse(self):
        length_type = get_bits(self.input_value, 1)
        if length_type == "0":
            sub_packet_size = int(get_bits(self.input_value, 15), 2)
            child_queue = Queue()
            [child_queue.put(i) for i in get_bits(self.input_value, sub_packet_size)]
            while not child_queue.empty():
                self.children.append(Packet.parse(child_queue))
        else:
            sub_packet_count = int(get_bits(self.input_value, 11), 2)
            for i in range(sub_packet_count):
                self.children.append(Packet.parse(self.input_value))

    def execute(self):
        result = 0
        children = [i.execute() for i in self.children]
        if self.packet_type == 0:
            result = sum(children)
        elif self.packet_type == 1:
            result = np.product(children)
        elif self.packet_type == 2:
            result = min(children)
        elif self.packet_type == 3:
            result = max(children)
        elif self.packet_type == 5:
            if children[0] > children[1]:
                result = 1
            else:
                result = 0
        elif self.packet_type == 6:
            if children[0] < children[1]:
                result = 1
            else:
                result = 0
        elif self.packet_type == 7:
            if children[0] == children[1]:
                result = 1
            else:
                result = 0
        return result

    def __str__(self) -> str:
        return f"Packet(v={self.version},t={self.packet_type},c={self.children})"


def read_input(file_name: str) -> Queue:
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        q = Queue()
        [q.put(i) for i in "".join(["{0:04b}".format(int(i, 16)) for i in lines[0]])]
        return q


def get_bits(input_value: Queue, quantity: int) -> str:
    value = ""
    for i in range(quantity):
        value += input_value.get()
    return value


def part1(packet: Packet) -> int:
    sum_versions = 0
    packets = [packet]
    while len(packets) != 0:
        packet = packets.pop()
        sum_versions += packet.version
        packets += packet.children

    return sum_versions


def part2(packet: Packet) -> int:
    return packet.execute()


if __name__ == "__main__":
    start = time.time()
    puzzle_input = Packet.parse(read_input("day16.txt"))
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
