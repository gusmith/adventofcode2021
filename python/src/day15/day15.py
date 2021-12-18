import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")


@dataclass(frozen=True)
class Mapie:
    mapie: Dict[Tuple[int, int], int]
    max_x: int
    max_y: int


def increase(current_val: int, increase: int) -> int:
    sol = current_val + increase
    while sol >= 10:
        sol -= 9
    return sol


def build_map_part2(mapie: Mapie) -> Mapie:
    bigger_mapie = copy.deepcopy(mapie.mapie)
    length_x = mapie.max_x + 1
    length_y = mapie.max_y + 1
    for key, value in mapie.mapie.items():
        for x in range(0, 5):
            for y in range(0, 5):
                increase_val = increase(value, x + y)
                i_x = key[0] + x * length_x
                i_y = key[1] + y * length_y
                bigger_mapie[(i_x, i_y)] = increase_val
    return Mapie(bigger_mapie, 5 * length_x - 1, 5 * length_y - 1)


def load_input(path_input_file) -> Mapie:
    mapie: Dict[Tuple[int, int], int] = {}
    with open(path_input_file, "r") as f:
        current_y = 0
        for row in f.readlines():
            if len(row.strip()) == 0:
                continue
            current_x = 0
            for c in row.strip():
                mapie[(current_x, current_y)] = int(c)
                current_x += 1
            current_y += 1
    return Mapie(mapie=mapie, max_x=current_x - 1, max_y=current_y - 1)


def next_step(
    mapie: Mapie,
    current_position_risks: Dict[Tuple[int, int], int],
    current_optimal_position_risks: Dict[Tuple[int, int], int],
) -> Tuple[Dict[Tuple[int, int], int], Dict[Tuple[int, int], int]]:
    optimals = copy.deepcopy(current_optimal_position_risks)
    sol: Dict[Tuple[int, int], int] = {}
    for key, value in current_position_risks.items():
        positions_to_try = []
        if key[0] > 1:
            # We can go left
            positions_to_try.append((key[0] - 1, key[1]))
        if key[0] < mapie.max_x:
            # We can go right
            positions_to_try.append((key[0] + 1, key[1]))
        if key[1] > 1:
            # We can go up
            positions_to_try.append((key[0], key[1] - 1))
        if key[1] < mapie.max_y:
            # We can go down
            positions_to_try.append((key[0], key[1] + 1))
        for possible_position in positions_to_try:
            risk_would_be = value + mapie.mapie[possible_position]
            if possible_position not in optimals:
                optimals[possible_position] = risk_would_be
                sol[possible_position] = risk_would_be
                continue
            if optimals[possible_position] > risk_would_be:
                # We found a better path to go there
                optimals[possible_position] = risk_would_be
                sol[possible_position] = risk_would_be
            # in the other case, we already arrived in this position in a
            # less risky path, so stop there
    return sol, optimals


def part1(mapie: Mapie) -> int:
    current_positions = {(0, 0): 0}
    optimals = {(0, 0): 0}
    while len(current_positions) > 0:
        current_positions, optimals = next_step(mapie, current_positions, optimals)
    return optimals[(mapie.max_x, mapie.max_y)]


def part2(mapie: Mapie) -> int:
    expended_mapie = build_map_part2(mapie)
    return part1(expended_mapie)


if __name__ == "__main__":
    input_mapie = load_input(path_input)

    print("# Part 1")
    sol_part1 = part1(input_mapie)
    print(f"Solution {sol_part1}")

    print("# Part 2")
    sol_part2 = part2(input_mapie)
    print(f"Solution {sol_part2}")
