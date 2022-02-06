from anytree import AsciiStyle, Node, PreOrderIter, RenderTree
from src.day18.day18 import (
    NAME_NODE_NOT_LEAF,
    compute_magnitude,
    create_tree,
    explode,
    part1,
    reduce,
    split,
    split_left_right,
)


def _compare_trees(tree1: Node, tree2: Node):
    # The equal method compares the object instances, not their values.
    list_leafs1 = [n for n in PreOrderIter(tree1)]
    list_leafs2 = [n for n in PreOrderIter(tree2)]
    assert len(list_leafs1) == len(list_leafs2), (
        f"Tree1:\n{str(RenderTree(tree1, style=AsciiStyle()))}"
        f"\nTree2:\n{str(RenderTree(tree2, style=AsciiStyle()))}"
    )
    for (a, b) in zip(list_leafs1, list_leafs2):
        assert a.name == b.name, (
            f"Tree1:\n{RenderTree(tree1, style=AsciiStyle())}"
            f"\nTree2:\n{RenderTree(tree1, style=AsciiStyle())}"
        )


def test_split_left_right():
    example1 = "12"
    assert split_left_right(example1) == ("1", "2")

    example2 = "[12]3"
    assert split_left_right(example2) == ("[12]", "3")

    example3 = "9[87]"
    assert split_left_right(example3) == ("9", "[87]")


def test_create_tree():
    example1 = "[12]"
    expected1 = Node(NAME_NODE_NOT_LEAF, children=[Node(1), Node(2)])
    _compare_trees(create_tree(example1), expected1)
    example2 = "[[12]3]"
    expected2 = Node(
        NAME_NODE_NOT_LEAF,
        children=[Node(NAME_NODE_NOT_LEAF, children=[Node(1), Node(2)]), Node(3)],
    )
    _compare_trees(create_tree(example2), expected2)
    example3 = "[9[87]]"
    expected3 = Node(
        NAME_NODE_NOT_LEAF,
        children=[Node(9), Node(NAME_NODE_NOT_LEAF, children=[Node(8), Node(7)])],
    )
    _compare_trees(create_tree(example3), expected3)
    example4 = "[[19][85]]"
    expected4 = Node(
        NAME_NODE_NOT_LEAF,
        children=[
            Node(NAME_NODE_NOT_LEAF, children=[Node(1), Node(9)]),
            Node(NAME_NODE_NOT_LEAF, children=[Node(8), Node(5)]),
        ],
    )
    _compare_trees(create_tree(example4), expected4)


def test_explode():
    example1 = create_tree("[[[[[98]1]2]3]4]")
    expected1 = create_tree("[[[[09]2]3]4]")
    assert explode(example1)
    _compare_trees(example1, expected1)

    example2 = create_tree("[7[6[5[4[32]]]]]")
    expected2 = create_tree("[7[6[5[70]]]]")
    assert explode(example2)
    _compare_trees(example2, expected2)

    example3 = create_tree("[[6[5[4[32]]]]1]")
    expected3 = create_tree("[[6[5[70]]]3]")
    assert explode(example3)
    _compare_trees(example3, expected3)

    example4 = create_tree("[[3[2[1[73]]]][6[5[4[32]]]]]")
    expected4 = create_tree("[[3[2[80]]][9[5[4[32]]]]]")
    assert explode(example4)
    _compare_trees(example4, expected4)

    example5 = create_tree("[[3[2[80]]][9[5[4[32]]]]]")
    expected5 = create_tree("[[3[2[80]]][9[5[70]]]]")
    assert explode(example5)
    _compare_trees(example5, expected5)


def test_split():
    example = create_tree("[[[[07]4][7[[84]9]]][11]]")
    assert explode(example)
    assert split(example)
    assert split(example)
    expected = create_tree("[[[[07]4][[78][0[67]]]][11]]")
    _compare_trees(example, expected)


def test_reduce():
    example = create_tree("[[[[[43]4]4][7[[84]9]]][11]]")
    reduce(example)
    expected = create_tree("[[[[07]4][[78][60]]][81]]")
    _compare_trees(example, expected)


def test_compute_magnitude():
    example1 = create_tree("[[12][[34]5]]")
    assert compute_magnitude(example1) == 143

    example2 = create_tree("[[[[07]4][[78][60]]][81]]")
    assert compute_magnitude(example2) == 1384

    example3 = create_tree("[[[[11][22]][33]][44]]")
    assert compute_magnitude(example3) == 445

    example4 = create_tree("[[[[30][53]][44]][55]]")
    assert compute_magnitude(example4) == 791

    example5 = create_tree("[[[[50][74]][55]][66]]")
    assert compute_magnitude(example5) == 1137

    example6 = create_tree("[[[[87][77]][[86][77]]][[[07][66]][87]]]")
    assert compute_magnitude(example6) == 3488


def test_part1():
    input = [
        create_tree(s)
        for s in [
            "[[[0[58]][[17][96]]][[4[12]][[14]2]]]",
            "[[[5[28]]4][5[[99]0]]]",
            "[6[[[62][56]][[76][47]]]]",
            "[[[6[07]][09]][4[9[90]]]]",
            "[[[7[64]][3[13]]][[[55]1]9]]",
            "[[6[[73][32]]][[[38][57]]4]]",
            "[[[[54][77]]8][[83]8]]",
            "[[93][[99][6[49]]]]",
            "[[2[[77]7]][[58][[93][02]]]]",
            "[[[[52]5][8[37]]][[5[75]][44]]]",
        ]
    ]
    part1_res = part1(input)
    assert part1_res == 4140
