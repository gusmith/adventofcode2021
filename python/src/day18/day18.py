import math
from pathlib import Path
from typing import List, Tuple

from anytree import Node, PreOrderIter

path_input = Path(__file__).parent.joinpath("input.txt")

NAME_NODE_NOT_LEAF = "n/a"


def load_input() -> List[Node]:
    list_trees = []
    with open(path_input, "r") as f:
        for line in f.readlines():
            tree = line.strip().replace(",", "")
            list_trees.append(create_tree(tree))
    return list_trees


def find_end_tree(line: str) -> int:
    current_open = 0
    for i, c in enumerate(line):
        if c == "[":
            current_open += 1
            continue
        if c == "]":
            current_open -= 1

        if current_open == 0:
            return i
    raise ValueError(f"Oopsie, there are some missing ']'.\n{line}")


def split_left_right(line: str) -> Tuple[str, str]:
    current_open = 0
    for i, c in enumerate(line):
        if c == "[":
            current_open += 1
            continue
        if c == "]":
            current_open -= 1
        if current_open == 0:
            return line[: i + 1], line[i + 1 :]
    raise ValueError("It should have closed!!!")


def create_tree(line: str) -> Node:
    if len(line) == 1:
        return Node(int(line))

    inside = line[1:-1]
    left, right = split_left_right(inside)
    return Node(NAME_NODE_NOT_LEAF, children=[create_tree(left), create_tree(right)])


def explode(tree: Node) -> bool:
    """BOOM!!!

    :param tree:
    :return: a boolean saying if the tree exploded, and the exploded
    tree if exploded, otherwise None
    """
    list_leafs: List[Node] = [n for n in PreOrderIter(tree) if n.is_leaf]
    for i in range(len(list_leafs) - 1):
        node1 = list_leafs[i]
        node2 = list_leafs[i + 1]
        if node1.depth >= 5 and node1.parent == node2.parent:
            # KABOOM
            if i > 0:
                list_leafs[i - 1].name += node1.name
            if i + 2 < len(list_leafs):
                list_leafs[i + 2].name += node2.name
            parent_parent = node1.parent.parent
            parent_parent.children = [n if n != node1.parent else Node(0, children=[]) for n in parent_parent.children]
            return True
    return False


def split(tree: Node) -> bool:
    list_leafs: List[Node] = [n for n in PreOrderIter(tree) if n.is_leaf]
    for leaf in list_leafs:
        if leaf.name >= 10:
            left = int(math.floor(leaf.name / 2.0))
            right = int(math.ceil(leaf.name / 2.0))
            leaf.name = NAME_NODE_NOT_LEAF
            leaf.children = [Node(left), Node(right)]
            return True
    return False


def addition(tree1: Node, tree2: Node) -> Node:
    return Node(NAME_NODE_NOT_LEAF, children=[tree1, tree2])


def reduce(tree: Node):
    while True:
        if explode(tree):
            continue
        if split(tree):
            continue
        break


def compute_magnitude(tree: Node) -> int:
    if tree.is_leaf:
        return tree.name
    return 3 * compute_magnitude(tree.children[0]) + 2 * compute_magnitude(tree.children[1])


def part1(list_inputs: List[Node]) -> int:
    sol = None
    for node in list_inputs:
        if sol is None:
            sol = node
            continue
        sol = addition(sol, node)
        reduce(sol)
    return compute_magnitude(sol)


def part2():
    length = len(load_input())
    max_sol = 0
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            # Must reload as we are changing the objects while computing.
            # The issue of having mutable objects
            inputs = load_input()
            current_tree = addition(inputs[i], inputs[j])
            reduce(current_tree)
            max_sol = max(max_sol, compute_magnitude(current_tree))
    return max_sol


if __name__ == "__main__":
    print("# Part 1")
    sol_part1 = part1(load_input())
    print(f"Solution {sol_part1}")

    print("# Part 2")
    sol_part2 = part2()
    print(f"Solution {sol_part2}")
