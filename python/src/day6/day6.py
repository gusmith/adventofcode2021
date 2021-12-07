from pathlib import Path
from typing import List

path_input = Path(__file__).parent.joinpath("input.txt")


def load_input():
    with open(path_input, "r") as f:
        elts = f.readline().strip().split(",")
    return elts


def next_step(li: List[int]) -> List[int]:
    a = [0] * 9
    a[0:8] = li[1:9]
    a[8] = li[0]
    a[6] += li[0]
    return a


def day6(nb_days):
    l = [0] * 9
    for e in load_input():
        l[int(e)] += 1
    print(f"Initial state {l}")
    for i in range(1, nb_days + 1):
        l = next_step(l)
    print(f"After {nb_days} day: {l}, sum {sum(l)}")


if __name__ == "__main__":
    print("# Part 1")
    day6(nb_days=80)

    print("# Part 2")
    day6(256)
