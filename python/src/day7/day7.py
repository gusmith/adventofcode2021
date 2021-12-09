from pathlib import Path

from numpy import median
from src.utils import get_one_line_input

path_input = Path(__file__).parent.joinpath("input.txt")


def day7(input_list):
    optimal = median(input_list)
    fuel_consumption = sum([abs(e - optimal) for e in input_list])
    print(f"Optimal point {optimal}, fuel cost {fuel_consumption}")
    return optimal, fuel_consumption


def day7_part2_brute_force(input_list):
    index_count = [0] * (max(input_list) + 1)
    for e in input_list:
        index_count[e] += 1

    def count(index):
        return sum(
            [
                x * abs(index - i) * (abs(index - i) + 1) / 2
                for i, x in enumerate(index_count)
            ]
        )

    min_consumption = None
    for i in range(0, len(index_count)):
        consumption = count(i)
        if min_consumption is None or min_consumption > consumption:
            min_consumption = consumption
            continue
        print(f"Min consumption {min_consumption} at index {i-1}")
        return i - 1, min_consumption


if __name__ == "__main__":
    print("# Part 1")
    part1_input = [int(e) for e in get_one_line_input(path_input)]
    day7(part1_input)

    print("# Part 2")
    part1_input = [int(e) for e in get_one_line_input(path_input)]
    day7_part2_brute_force(part1_input)
