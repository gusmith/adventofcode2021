import math
from collections import defaultdict
from pathlib import Path
from typing import Dict, Set, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")


def load_input() -> Tuple[str, Dict[str, str]]:
    with open(path_input, "r") as f:
        rules = {}
        polymer = ""
        for row in f.readlines():
            if len(row.strip()) == 0:
                continue
            if " -> " in row:
                splitted = row.split(" -> ")
                rules[splitted[0].strip()] = splitted[1].strip()
                continue
            if len(polymer) > 0:
                raise ValueError("The row seems to contain a polymer, but it should not...")
            polymer = row.strip()
    return polymer, rules


def split_str_into_map_binoms(the_string: str) -> Dict[str, int]:
    sol: Dict[str, int] = defaultdict(int)
    for i in range(0, len(the_string) - 1):
        sol[the_string[i : i + 2]] += 1
    return sol


def one_step(before: Dict[str, int], rules: Dict[str, str]) -> Dict[str, int]:
    sol: Dict[str, int] = defaultdict(int)
    for key, value in before.items():
        new_letter = rules[key]
        sol[f"{key[0]}{new_letter}"] += value
        sol[f"{new_letter}{key[1]}"] += value
    return sol


def part1(list_polymer: str, rules: Dict[str, str], nb_steps: int) -> int:
    out = split_str_into_map_binoms(list_polymer)
    for i in range(0, nb_steps):
        out = one_step(out, rules)
    counters: Dict[str, int] = defaultdict(int)
    for key, value in out.items():
        counters[key[0]] += value
        counters[key[1]] += value
    for key, value in counters.items():
        counters[key] = math.ceil(float(value) / 2.0)
    return max(counters.values()) - min(counters.values())


def print_points(list_points: Set[Tuple[int, int]]):
    max_x = max([a[0] for a in list_points])
    max_y = max([a[1] for a in list_points])
    sol = [["."] * (max_x + 1) for _ in range(max_y + 1)]
    for point in list_points:
        sol[point[1]][point[0]] = "#"
    string_to_print = "\n".join(["".join(row) for row in sol])
    print(string_to_print)


if __name__ == "__main__":
    input_polymer, input_rules = load_input()

    print("# Part 1")
    sol_part1 = part1(input_polymer, input_rules, 10)
    print(f"Solution {sol_part1}")

    print("# Part 1")
    sol_part1 = part1(input_polymer, input_rules, 40)
    print(f"Solution {sol_part1}")
