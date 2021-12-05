from pathlib import Path

from src.utils import get_csv_line_iterator

path_input = Path(__file__).parent.joinpath("input.csv")


def puzzle1():
    x = 0
    depth = 0
    for row in get_csv_line_iterator(path_input):
        action, str_value = row[0].split(" ")
        value = int(str_value)
        if action == "forward":
            x += value
        elif action == "down":
            depth += value
        elif action == "up":
            depth -= value
        else:
            print(f"unknown action {action}")
    solution = x * depth
    return x, depth, solution


def puzzle2():
    x = 0
    depth = 0
    aim = 0
    for row in get_csv_line_iterator(path_input):
        action, str_value = row[0].split(" ")
        value = int(str_value)
        if action == "forward":
            x += value
            depth += aim * value
        elif action == "down":
            aim += value
        elif action == "up":
            aim -= value
        else:
            print(f"unknown action {action}")
    solution = x * depth
    return x, depth, solution


if __name__ == "__main__":
    print("# Puzzle 1")
    _x, _depth, _solution = puzzle1()
    print(f"x={_x}, depth={_depth}")
    print(f"solution is {_solution}")

    print("# Puzzle 2")
    _x, _depth, _solution = puzzle2()
    print(f"x={_x}, depth={_depth}")
    print(f"solution is {_solution}")
