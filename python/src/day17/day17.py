import math
from enum import Enum, auto
from typing import List, Tuple


class Shoot(Enum):
    BEFORE = auto()
    IN = auto()
    PASSED = auto()


def where_compared_to_zone(
    current_pos: Tuple[int, int], range_x: Tuple[int, int], range_y: Tuple[int, int]
) -> Shoot:
    x, y = current_pos
    if x > range_x[1] or y < range_y[0]:
        return Shoot.PASSED
    if x < range_x[0] or y > range_y[1]:
        return Shoot.BEFORE
    return Shoot.IN


def check_this_curve(
    init_speed: Tuple[int, int], target_x: Tuple[int, int], target_y: Tuple[int, int]
) -> bool:
    x = 0
    y = 0
    v_x, v_y = init_speed
    current_shoot = where_compared_to_zone((x, y), target_x, target_y)
    while current_shoot == Shoot.BEFORE:
        x += v_x
        v_x = max(0, v_x - 1)
        y += v_y
        v_y -= 1
        current_shoot = where_compared_to_zone((x, y), target_x, target_y)
    return current_shoot == Shoot.IN


def brute_force(target_x: Tuple[int, int], target_y: Tuple[int, int]):
    working_speeds = []
    for v_x in range(int(math.sqrt(2 * target_x[0])), target_x[1] + 1):
        for v_y in range(target_y[0], abs(target_y[0]) + 1):
            if check_this_curve((v_x, v_y), target_x, target_y):
                working_speeds.append((v_x, v_y))
    return working_speeds


def compute_part1(_working_speeds: List[Tuple[int, int]]) -> int:
    max_vy = max([a[1] for a in _working_speeds])
    return int(max_vy * (max_vy + 1) / 2)


if __name__ == "__main__":
    input_area = {"x": (85, 145), "y": (-163, -108)}

    working_speeds = brute_force(input_area["x"], input_area["y"])

    print("# Part 1")
    sol_part1 = compute_part1(working_speeds)
    print(f"Solution {sol_part1}")

    print("# Part 2")
    sol_part2 = len(working_speeds)
    print(f"Solution {sol_part2}")
