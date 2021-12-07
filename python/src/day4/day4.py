from pathlib import Path
from typing import List, Optional, Tuple

path_input = Path(__file__).parent.joinpath("input.txt")


class Board:
    def __init__(self, lines_str: List[str]):
        assert len(lines_str) == 5, "A board should only have 5 lines"
        self.board: List[List[int]] = [
            [int(nb) for nb in s.strip().replace("  ", " ").split(" ")]
            for s in lines_str
        ]
        assert len(self.board) == 5
        for e in self.board:
            assert len(e) == 5

    def check_finished(self) -> bool:
        for i in range(len(self.board)):
            if set(self.board[i][:]) == {-1} or set([row[i] for row in self.board]) == {
                -1
            }:
                return True
        # if {self.board[i][i] for i in range(len(self.board))} == {-1} or {self.board[i][len(self.board) - i - 1] for i in range(len(self.board))} == {-1}:
        #     return True
        return False

    def sum_remaining_element(self) -> int:
        return sum([sum([e for e in row if e != -1]) for row in self.board])

    def check_number(self, nb: int) -> bool:
        res = False
        for id_x, row in enumerate(self.board):
            for id_y, val in enumerate(row):
                if val == nb:
                    self.board[id_x][id_y] = -1
                    res = True
        return res

    def new_number(self, nb: int) -> Tuple[bool, Optional[int]]:
        if self.check_number(nb) and self.check_finished():
            return True, self.sum_remaining_element()
        else:
            return False, None

    def pretty_print(self):
        for row in self.board:
            _row = [str(e) if e != -1 else "X" for e in row]
            print(", ".join(_row))


class SolverPart1:
    def __init__(self):
        self.boards = []
        self.list_selected_balls = None
        with open(path_input, "r") as f:
            first_line = f.readline()
            self.list_selected_balls = [int(s) for s in first_line.strip().split(",")]

            current_board = []
            for row in f:
                if row.strip() == "":
                    continue
                current_board.append(row)
                if len(current_board) == 5:
                    self.boards.append(Board(current_board))
                    current_board = []

        print(len(self.boards))

    def iterate_over_boards(self, nb: int) -> Optional[int]:
        for idx, board in enumerate(self.boards):
            is_bingo, end_value = board.new_number(nb)
            # print(f"\nBoard {idx}")
            # board.pretty_print()
            if is_bingo:
                return nb * end_value
        return None

    def iterate_over_balls(self):
        for ball in self.list_selected_balls:
            # print(f"\n# Ball {ball}")
            a = self.iterate_over_boards(ball)
            if a:
                print(f"The result is {a}")
                break


class SolverPart2(SolverPart1):
    def iterate_over_boards(self, nb: int) -> Optional[int]:
        boards_to_remove = []
        for board in self.boards:
            # print(f"Before number {nb}")
            # board.pretty_print()
            is_bingo, end_value = board.new_number(nb)
            # print()
            # board.pretty_print()
            if is_bingo:
                if len(self.boards) == 1:
                    board.pretty_print()
                    return nb * end_value
                else:
                    # print("")
                    # board.pretty_print()
                    boards_to_remove.append(board)
        for b in boards_to_remove:
            # print(len(self.boards))
            self.boards.remove(b)
            # print(len(self.boards))
        return None


if __name__ == "__main__":
    print("# Part 1")
    solver = SolverPart1()
    solver.iterate_over_balls()

    print("\n#Part 2")
    solver2 = SolverPart2()
    solver2.iterate_over_balls()
