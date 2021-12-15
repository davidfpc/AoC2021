# program to compute the time of execution of any python code
import heapq
import time


def read_input(file_name: str) -> [[int]]:
    with open("inputFiles/" + file_name, "r") as file:
        lines = file.read().splitlines()
        return [[int(i) for i in z] for z in lines]


class Graph(object):
    def __init__(self, input_value):
        self.input_value = input_value

    def get_nodes(self):
        """Returns the nodes of the graph."""
        return [(x, y) for x in range(len(self.input_value[0])) for y in range(len(self.input_value))]

    def get_outgoing_edges(self, node):
        """Returns the neighbors of a node."""
        x, y = node
        connections = [(x + x_delta, y + y_delta) for x_delta, y_delta in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 0)]]  # right, down, left, up
        return [(x, y) for x, y in connections if 0 <= x < len(self.input_value[0]) and 0 <= y < len(self.input_value)]

    def value(self, node2):
        """Returns the value of an edge between two nodes."""
        x, y = node2
        return self.input_value[y][x]


def part1(input_value: [[int]]):
    graph = Graph(input_value)
    shortest_path = dijkstra_algorithm(graph, (0, 0))
    return shortest_path[(len(input_value[0]) - 1, len(input_value[0]) - 1)]


def dijkstra_algorithm(graph: Graph, starting_vertex: (int, int)):
    """Copied and adapted from https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/"""
    distances = {vertex: float('infinity') for vertex in graph.get_nodes()}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph.get_outgoing_edges(current_vertex):
            weight = graph.value(neighbor)
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def part2(input_value: [[int]]) -> int:
    # expand to the side
    original_x_length = len(input_value[0])
    for y in range(len(input_value)):
        for x in range(original_x_length, original_x_length * 5):
            new_value = input_value[y][x - original_x_length] % 9 + 1
            input_value[y].append(new_value)
    # expand down
    original_y_length = len(input_value)
    for y in range(original_y_length, len(input_value) * 5):
        input_value.append([input_value[y - original_y_length][x] % 9 + 1 for x in range(len(input_value[0]))])

    graph = Graph(input_value)
    shortest_path = dijkstra_algorithm(graph, (0, 0))
    result = shortest_path[(len(input_value[0]) - 1, len(input_value[0]) - 1)]

    return result


if __name__ == "__main__":
    puzzle_input = read_input("day15.txt")
    start = time.time()
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
    end = time.time()
    print(f"Took {round(end - start, 5)} to process the puzzle")
