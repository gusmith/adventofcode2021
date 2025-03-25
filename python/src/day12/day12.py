import copy
from pathlib import Path
from typing import Dict, List, Set, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")


def load_input() -> List[Tuple[str, str]]:
    with open(path_input, "r") as f:
        out: List[Tuple[str, str]] = []
        for row in f.readlines():
            elts = row.strip().split("-")
            out.append((elts[0], elts[1]))
        return out


def list_path_to_map_paths(list_paths: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
    sol = {}
    for path in list_paths:
        paths = [path, path[::-1]]
        for _path in paths:
            if _path[0] not in sol:
                sol[_path[0]] = {_path[1]}
            else:
                sol[_path[0]].add(_path[1])
    # We cannot leave 'end', so stop there
    sol.pop("end")
    return sol


def _check_if_already_visited_twice_same_small_caverns(path: List[str]) -> bool:
    list_small_caverns = [e for e in path if e.islower()]
    return len(list_small_caverns) != len(set(list_small_caverns))


def part1(list_paths: List[Tuple[str, str]], double_1_small_cave: bool = False) -> int:
    map_paths = list_path_to_map_paths(list_paths)
    paths = [["start"]]
    nb_finished_paths = 0
    while len(paths) > 0:
        available_path = paths.pop()
        next_possible_steps = map_paths[available_path[-1]]
        for step in next_possible_steps:
            if step == "start":
                #
                continue
            if step == "end":
                nb_finished_paths += 1
                continue
            # Case where it's a small cave, and we already went in, so not possible path
            if step.islower() and step in available_path:
                if not double_1_small_cave or _check_if_already_visited_twice_same_small_caverns(available_path):
                    continue
            p = copy.deepcopy(available_path)
            p.append(step)
            paths.append(p)
    return nb_finished_paths


def part2(list_paths: List[Tuple[str, str]]) -> int:
    return part1(list_paths, True)


if __name__ == "__main__":
    input_day12 = load_input()

    print("# Part 1")
    sol_part1 = part1(input_day12)
    print(f"Solution {sol_part1}")

    print("# Part 2")
    sol_part2 = part2(input_day12)
    print(f"Solution {sol_part2}")
