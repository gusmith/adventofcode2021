import copy
from pathlib import Path
from typing import List, Set, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")


def load_input() -> Tuple[Set[Tuple[int, int]], List[Tuple[str, int]]]:
    with open(path_input, "r") as f:
        list_points = set()
        list_folds = []
        for row in f.readlines():
            if len(row.strip()) == 0:
                continue
            if row.startswith("fold along"):
                content = row[len("fold along ") :].strip()
                splitouille = content.split("=")
                list_folds.append((splitouille[0], int(splitouille[1])))
                continue
            splittouille_again = row.strip().split(",")

            list_points.add((int(splittouille_again[0]), int(splittouille_again[1])))
        return list_points, list_folds


def recenter(list_points: Set[Tuple[int, int]]):
    min_x = min([a[0] for a in list_points])
    min_y = min([a[1] for a in list_points])
    moved_points = {
        (
            point[0] + min_x if min_x < 0 else point[0],
            point[1] + min_y if min_y < 0 else point[1],
        )
        for point in list_points
    }
    return moved_points


def part1(
    list_points: Set[Tuple[int, int]], fold: Tuple[str, int]
) -> Set[Tuple[int, int]]:
    list_points_after_fold = set()
    axis = fold[0]
    val = fold[1]
    assert axis in ["x", "y"]
    for point in list_points:
        if axis == "x":
            if point[0] < val:
                list_points_after_fold.add(point)
                continue
            if point[0] > val:
                list_points_after_fold.add((2 * val - point[0], point[1]))
                continue
        if point[1] < val:
            list_points_after_fold.add(point)
            continue
        if point[1] > val:
            list_points_after_fold.add((point[0], 2 * val - point[1]))
    return recenter(list_points_after_fold)


def print_points(list_points: Set[Tuple[int, int]]):
    max_x = max([a[0] for a in list_points])
    max_y = max([a[1] for a in list_points])
    sol = [["."] * (max_x + 1) for _ in range(max_y + 1)]
    for point in list_points:
        sol[point[1]][point[0]] = "#"
    string_to_print = "\n".join(["".join(row) for row in sol])
    print(string_to_print)


def part2(
    list_paths: Set[Tuple[int, int]], folds: List[Tuple[str, int]]
) -> Set[Tuple[int, int]]:
    sol = copy.deepcopy(list_paths)
    for fold in folds:
        sol = part1(sol, fold)
    return sol


if __name__ == "__main__":
    input_day13, folds_inputs = load_input()

    print("# Part 1")
    sol_part1 = part1(input_day13, folds_inputs[0])
    print(f"Solution {len(sol_part1)}")

    print("# Part 2")
    sol_part2 = part2(input_day13, folds_inputs)
    print_points(sol_part2)
