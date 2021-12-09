from pathlib import Path
from typing import List

from src.utils import get_one_line_input

path_input = Path(__file__).parent.joinpath("input.txt")


def next_step(li: List[int]) -> List[int]:
    a = [0] * 9
    a[0:8] = li[1:9]
    a[8] = li[0]
    a[6] += li[0]
    return a


def day6(nb_days):
    sol = [0] * 9
    for e in get_one_line_input(path_input):
        sol[int(e)] += 1
    print(f"Initial state {sol}")
    for i in range(1, nb_days + 1):
        sol = next_step(sol)
    print(f"After {nb_days} day: {sol}, sum {sum(sol)}")


if __name__ == "__main__":
    print("# Part 1")
    day6(nb_days=80)

    print("# Part 2")
    day6(256)
