import copy
from pathlib import Path
from typing import List, Set, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")


def load_input() -> List[Tuple[List[str], List[str]]]:
    end_list = []
    with open(path_input, "r") as f:
        for row in f:
            splittouille = row.strip().split(" | ")
            assert len(splittouille) == 2
            t = (splittouille[0].split(" "), splittouille[1].split(" "))
            assert len(t[0]) == 10
            assert len(t[1]) == 4
            end_list.append(t)
    return end_list


def day8_part1(input_list: List[Tuple[List[str], List[str]]]) -> int:
    return sum([sum([1 for e in a[1] if len(e) in [2, 3, 4, 7]]) for a in input_list])


class SolverPart2:
    def __init__(self, number_1: Set[str], number_4: Set[str], number_7: Set[str]):
        self.number_1 = number_1
        self.number_4 = number_4
        self.number_7 = number_7

    def is_number_0(self, this_number: Set[str]) -> bool:
        return (
            len(this_number) == 6
            and this_number.issuperset(self.number_1)
            and len(this_number.intersection(self.number_4)) == 3
            and this_number.issuperset(self.number_7)
        )

    def is_number_2(self, this_number: Set[str]) -> bool:
        return (
            len(this_number) == 5
            and len(this_number.intersection(self.number_1)) == 1
            and len(this_number.intersection(self.number_4)) == 2
            and len(this_number.intersection(self.number_7)) == 2
        )

    def is_number_3(self, this_number: Set[str]) -> bool:
        return (
            len(this_number) == 5
            and this_number.issuperset(self.number_1)
            and len(this_number.intersection(self.number_4)) == 3
            and this_number.issuperset(self.number_7)
        )

    def is_number_5(self, this_number: Set[str]) -> bool:
        return (
            len(this_number) == 5
            and len(this_number.intersection(self.number_1)) == 1
            and len(this_number.intersection(self.number_4)) == 3
            and len(this_number.intersection(self.number_7)) == 2
        )

    def is_number_6(self, this_number: Set[str]) -> bool:
        return (
            len(this_number) == 6
            and len(this_number.intersection(self.number_1)) == 1
            and len(this_number.intersection(self.number_4)) == 3
            and len(this_number.intersection(self.number_7)) == 2
        )

    def is_number_9(self, this_number: Set[str]) -> bool:
        return (
            len(this_number) == 6
            and this_number.issuperset(self.number_1)
            and this_number.issuperset(self.number_4)
            and this_number.issuperset(self.number_7)
        )

    def find_number(self, this_number: str) -> int:
        this_number_set = set(this_number)
        if len(this_number) == 7:
            return 8
        if self.is_number_0(this_number_set):
            return 0
        if this_number_set == self.number_1:
            return 1
        if self.is_number_2(this_number_set):
            return 2
        if self.is_number_3(this_number_set):
            return 3
        if this_number_set == self.number_4:
            return 4
        if self.is_number_5(this_number_set):
            return 5
        if self.is_number_6(this_number_set):
            return 6
        if this_number_set == self.number_7:
            return 7
        if self.is_number_9(this_number_set):
            return 9
        raise ValueError("PwomPwom")


def solve(single_row: Tuple[List[str], List[str]]) -> int:
    full_list = copy.deepcopy(single_row[0])
    full_list.extend(copy.deepcopy(single_row[1]))
    number_1 = set([a for a in full_list if len(a) == 2][0])
    number_4 = set([a for a in full_list if len(a) == 4][0])
    number_7 = set([a for a in full_list if len(a) == 3][0])
    # number_8 = [a for a in full_list if len(a) == 7][0]

    solver = SolverPart2(number_1, number_4, number_7)
    sol = 0
    for a in single_row[1]:
        sol = sol * 10 + solver.find_number(a)
    return sol


def day8_part2(input_list: List[Tuple[List[str], List[str]]]) -> List[int]:
    return [solve(a) for a in input_list]
    # return sum(sol_list)


if __name__ == "__main__":
    print("# Part 1")
    input_part1 = load_input()
    sol_part1 = day8_part1(input_part1)
    print(f"The sol is {sol_part1}")

    print("# Part 2")
    input_part2 = load_input()
    sol_part2_list = day8_part2(input_part2)
    sol_part2 = sum(sol_part2_list)
    print(f"The sol is {sol_part2}")
