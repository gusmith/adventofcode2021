import copy
from pathlib import Path
from typing import List, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")


def load_input() -> List[List[int]]:
    with open(path_input, "r") as f:
        return [[int(elt) for elt in row.strip()] for row in f.readlines()]


def increase_adjacent(
    current_state: List[List[int]], current_x: int, current_y: int
) -> Tuple[List[List[int]], List[Tuple[int, int]]]:
    """Explose all the adjacent cases and return a list of all the newly
    exploded cases.

    :param current_state:
    :param current_x:
    :param current_y:
    :return: the new state after this explosion, and the new cases to explode.
    """
    set_x = {current_x}
    if current_x > 0:
        set_x.add(current_x - 1)
    if current_x < len(current_state) - 1:
        set_x.add(current_x + 1)
    set_y = {current_y}
    if current_y > 0:
        set_y.add(current_y - 1)
    if current_y < len(current_state) - 1:
        set_y.add(current_y + 1)
    new_state = copy.deepcopy(current_state)
    new_state[current_x][current_y] = 0
    list_new_to_explode = []
    for x in set_x:
        for y in set_y:
            if x == current_x and y == current_y:
                continue
            if new_state[x][y] > 0:
                new_state[x][y] += 1
            if new_state[x][y] > 9:
                list_new_to_explode.append((x, y))
    return new_state, list_new_to_explode


def one_step(current_state: List[List[int]]) -> Tuple[List[List[int]], int]:
    new_step = [[elt + 1 for elt in row] for row in current_state]
    set_to_explode = {(x, y) for x, row in enumerate(current_state) for y, elt in enumerate(row) if elt == 9}
    nb_exploded = 0
    while len(set_to_explode) != 0:
        elt = set_to_explode.pop()
        new_step, newly_exploded = increase_adjacent(new_step, elt[0], elt[1])
        nb_exploded += 1
        for e in newly_exploded:
            set_to_explode.add(e)
    return new_step, nb_exploded


def part1(start_state: List[List[int]], nb_steps: int) -> int:
    total_explosions = 0
    new_step = copy.deepcopy(start_state)
    for _ in range(nb_steps):
        new_step, nb_explo = one_step(new_step)
        total_explosions += nb_explo
    return total_explosions


def part2(start_state: List[List[int]], mx_nb_steps: int) -> int:
    new_step = copy.deepcopy(start_state)
    expected_nb_explosions = len(start_state) * len(start_state[0])
    for step in range(1, mx_nb_steps + 1):
        new_step, nb_explo = one_step(new_step)
        if nb_explo == expected_nb_explosions:
            return step
    raise ValueError("The max number of steps provided is to small")


if __name__ == "__main__":
    input_day11 = load_input()

    print("# Part 1")
    sol_part1 = part1(input_day11, 100)
    print(f"Solution {sol_part1}")

    print("# Part 2")
    sol_part2 = part2(input_day11, 1000)
    print(f"Solution {sol_part2}")
