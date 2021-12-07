from pathlib import Path
from typing import Tuple

import numpy as np
from numpy import ndarray

path_input = Path(__file__).parent.joinpath("input.txt")


def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    line = line.strip()
    splittouille = line.split("->")
    assert len(splittouille) == 2
    first = tuple(int(e) for e in splittouille[0].split(","))
    second = tuple(int(e) for e in splittouille[1].split(","))
    assert len(first) == len(second) == 2
    return first, second


def day5(with_diagonal: bool):
    sol = np.zeros(shape=(1000, 1000), dtype=int)
    with open(path_input, "r") as f:
        for line in f:
            first, second = parse_line(line)
            max_x = max(first[0], second[0])
            max_y = max(first[1], second[1])
            min_x = min(first[0], second[0])
            min_y = min(first[1], second[1])
            # if sol.shape[0] <= max_x or sol.shape[1] <= max_y:
            #     new_x = max(max_x + 1, sol.shape[0])
            #     new_y = max(max_y + 1, sol.shape[1])
            #     sol = np.resize(sol, (new_x, new_y))
            if min_x == max_x:
                for y in range(min_y, max_y + 1):
                    sol[min_x][y] += 1
                continue
            if min_y == max_y:
                for x in range(min_x, max_x + 1):
                    sol[x][min_y] += 1
                continue
            if max_x - min_x == max_y - min_y and with_diagonal:
                cond_x = 1 if second[0] > first[0] else -1
                cond_y = 1 if second[1] > first[1] else -1
                for (x, y) in zip(
                    range(first[0], second[0] + cond_x, cond_x),
                    range(first[1], second[1] + cond_y, cond_y),
                ):
                    sol[x][y] += 1
                continue
    return np.sum(np.ones(shape=sol.shape), where=(sol > 1), dtype=int)


if __name__ == "__main__":
    print("# Part 1")
    _sol = day5(False)
    print(f"sol {_sol}")

    print("\n# Part 2")
    _sol2 = day5(True)
    print(f"sol {_sol2}")
