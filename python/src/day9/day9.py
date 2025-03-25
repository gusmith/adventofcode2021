import math
from pathlib import Path
from typing import Dict, List, Optional, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")


def load_input() -> List[List[int]]:
    end_list = []
    with open(path_input, "r") as f:
        for row in f:
            end_list.append([int(c) for c in row.strip()])
    return end_list


def part1(heatmap: List[List[int]]) -> int:
    valid_indices: List[Tuple[int, int]] = []
    for x, row in enumerate(heatmap):
        can_be = False
        previous = None
        for y, elt in enumerate(row):
            if previous is None:
                previous = elt
                can_be = True
                continue
            if previous < elt:
                if can_be:
                    valid_indices.append((x, y - 1))
                    can_be = False
            elif elt < previous:
                can_be = True
            else:
                can_be = False
            previous = elt
        if can_be:
            valid_indices.append((x, y))

    solution = 0
    for x, y in valid_indices:
        val = heatmap[x][y]
        if (
            (x == 0 and val < heatmap[x + 1][y])
            or (x == len(heatmap) - 1 and val < heatmap[x - 1][y])
            or (val < heatmap[x - 1][y] and val < heatmap[x + 1][y])
        ):
            solution += val + 1
    return solution


def part2(heatmap: List[List[int]]) -> int:
    """The idea in this part is go over all elements, one at a time, and
    looking on its left and top. It is important to note that the only part to
    keep in memory are the borders, and the counters. If:

    - the new point as a value of 9, it's part of the border (and thus
    no group, represented with None)
    - they are already in the same
    group, all good, the three points are in the same group.
    - the top and left are in no groups (i.e borders), this new point is part
     of a new group (as far as we currently know)
    - the point only has one neighbor, they are in the same group
    - the point is neighboring two points from different groups, we can merge
     these two groups, which means updating the current indices about these
     groups to point to one and sum their counters together, adding the
     current point to the group too.
    """
    length_row = len(heatmap[0])
    # Where we will map the group index to the number of points in it
    group_count: Dict[int, int] = {}
    # Last row processed, which include group indices, not the depth value
    last_group_line: List[Optional[int]] = [None] * length_row
    # Counter to know what will be the group index of the next group to create
    new_group = 0
    for x, row in enumerate(heatmap):
        # Where we store the current row group indices
        current_row: List[Optional[int]] = [None] * len(heatmap[0])
        # Group index of the point left to the current one.
        last_group = None
        for y, elt in enumerate(row):
            if elt == 9:
                # one of the border, in no group
                last_group = None
                continue
            # read the value from the previous line
            top_group = last_group_line[y]
            if top_group is None and last_group is None:
                # The current point, has not neighbor, and is not a border.
                # Create a new group
                current_row[y] = new_group
                last_group = new_group
                group_count[new_group] = 1
                new_group += 1
            elif top_group is None or last_group is None:
                # Bordering just one other point.=, thus share the same group
                current_group = top_group if top_group is not None else last_group
                if current_group is None:
                    raise ValueError("It should not have happened.")
                current_row[y] = current_group
                last_group = current_group
                group_count[current_group] += 1
            else:
                # Bordering two points (left and top)
                if last_group == top_group:
                    # All in the same group, easy :)
                    current_row[y] = last_group
                    group_count[last_group] += 1
                else:
                    # Merging group, keeping the left because why not
                    group_count[last_group] += group_count.pop(top_group) + 1
                    last_group_line = [last_group if e == top_group else e for e in last_group_line]
                    current_row = [last_group if e == top_group else e for e in current_row]
                    current_row[y] = last_group
        last_group_line = current_row

    # Finally, keeping only the three groups with the highest number of points in
    counts = list(group_count.values())
    counts.sort(reverse=True)
    return math.prod(counts[0:3])


if __name__ == "__main__":
    print("# Part 1")
    heatmap_input = load_input()
    sol = part1(heatmap_input)
    print(f"Solution {sol}")

    print("# Part 2")
    sol = part2(heatmap_input)
    print(f"Solution {sol}")
