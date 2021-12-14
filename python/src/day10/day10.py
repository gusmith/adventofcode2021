from pathlib import Path
from typing import List, Tuple

import numpy as np

path_input = Path(__file__).parent.joinpath("input.txt")

mapped_chars = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

mapped_score_illegal = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

mapped_score_not_finished = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def load_input() -> List[str]:
    end_list = []
    with open(path_input, "r") as f:
        for row in f:
            end_list.append(row.strip())
    return end_list


def handle_row(row: str) -> Tuple[int, int]:
    """
    Handles a row for both use case.
    First returned int is for the illegal case, the second for the unfinished row
    :param row:
    :return:
    """
    s = ""
    for character in row:
        if character in ['[', '(', '<', '{']:
            s += character
        else:
            last_opened_char = s[-1]
            if last_opened_char == mapped_chars[character]:
                s = s[:-1]
            else:
                # illegal
                return mapped_score_illegal[character], 0
    sol = 0
    for i in range(len(s)-1, -1, -1):
        sol = sol * 5 + mapped_score_not_finished[s[i]]
    return -1, sol


def part1(str_list: List[str]) -> int:
    sol = 0
    for row in str_list:
        sol += handle_row(row)[0]
    return sol


def part2(str_list: List[str]) -> int:
    sol = []
    for row in str_list:
        illegal_val, incomplete = handle_row(row)
        if illegal_val == -1:
            sol.append(incomplete)
    return int(np.median(sol))


if __name__ == '__main__':
    input_day10 = load_input()

    print("# Part 1")
    sol_part1 = part1(input_day10)
    print(f"Solution {sol_part1}")

    print("# Part 2")
    sol_part2 = part2(input_day10)
    print(f"Solution {sol_part2}")