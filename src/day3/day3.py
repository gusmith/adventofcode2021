from pathlib import Path
from typing import List

from src.utils import get_csv_line_iterator

path_input = Path(__file__).parent.joinpath("input.csv")


def _bit_list_to_int(l: List[int]):
    val = 0
    for bit in l:
        val = (val << 1) | bit
    return val


def day3_1():
    counter_bits = None
    counter_words = 0
    for row in get_csv_line_iterator(path_input):
        value = row[0]
        if counter_bits is None:
            counter_bits = [0] * len(value)
        for index, character in enumerate(value):
            if character == "1":
                counter_bits[index] += 1
        counter_words += 1
    gamma_list = [1 if 2 * e > counter_words else 0 for e in counter_bits]
    epsilon_list = [1 - e for e in gamma_list]
    gamma = _bit_list_to_int(gamma_list)
    epsilon = _bit_list_to_int(epsilon_list)
    power = gamma * epsilon
    return gamma, epsilon, power


def day3_2():
    pass


if __name__ == "__main__":
    # Part 1
    _gamma, _epsilon, _power = day3_1()
    print(f"gamma {_gamma}, epsilon {_epsilon}, power {_power}")
