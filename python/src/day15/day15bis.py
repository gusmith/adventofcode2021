import copy
from dataclasses import dataclass
from pathlib import Path
from queue import PriorityQueue
from typing import Dict, List, Optional, Tuple

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


def using_priority_queue(
    mapie: Mapie,
    position_to_check: Tuple[int, int],
    associated_value: int,
    current_optimal_position_risks: Dict[Tuple[int, int], int],
    current_best: int | None = None,
) -> Tuple[List[Tuple[Tuple[int, int], int]], Dict[Tuple[int, int], int], Optional[int]]:
    positions_to_try = []
    sol = []
    if current_best is not None and associated_value > current_best:
        return [], current_optimal_position_risks, current_best
    if position_to_check[0] > 1:
        # We can go left
        positions_to_try.append((position_to_check[0] - 1, position_to_check[1]))
    if position_to_check[0] < mapie.max_x:
        # We can go right
        positions_to_try.append((position_to_check[0] + 1, position_to_check[1]))
    if position_to_check[1] > 1:
        # We can go up
        positions_to_try.append((position_to_check[0], position_to_check[1] - 1))
    if position_to_check[1] < mapie.max_y:
        # We can go down
        positions_to_try.append((position_to_check[0], position_to_check[1] + 1))
    for possible_position in positions_to_try:
        risk_would_be = associated_value + mapie.mapie[possible_position]
        if current_best is not None and risk_would_be > current_best:
            continue
        if (
            possible_position not in current_optimal_position_risks
            or current_optimal_position_risks[possible_position] > risk_would_be
        ):
            current_optimal_position_risks[possible_position] = risk_would_be
            sol.append((possible_position, risk_would_be))
        if possible_position == (mapie.max_x, mapie.max_y):
            current_best = risk_would_be
    return sol, current_optimal_position_risks, current_best


def part1(mapie: Mapie) -> int:
    """Way faster implementation that the first day15. Using a priority queue
    to order the elements to process in order improves drastically timing +
    implementation of filtering (not processing paths already longer than the
    best solution)

    :param mapie:
    :return:
    """
    position_queue: PriorityQueue[Tuple[int, Tuple[int, int]]] = PriorityQueue()
    position_queue.put((0, (0, 0)))
    optimals = {(0, 0): 0}
    current_best = None

    while not position_queue.empty():
        elt = position_queue.get()
        list_new_points, optimals, current_best = using_priority_queue(mapie, elt[1], elt[0], optimals, current_best)
        for p in list_new_points:
            position_queue.put((p[1], p[0]))
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
