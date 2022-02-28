import random
from copy import copy, deepcopy
from typing import final
from typing_extensions import Self


class Taquin:

    def __init__(self):
        self.n: int = 3  # Board's height and width
        self.depth: int = 0
        # Instantiating the Taquin with random values
        self.board_numbers: dict[int, int] = {}
        coordinates_list: list[tuple(int, int)] = [(i, j) for i in range(self.n) for j in range(self.n)]
        random.shuffle(coordinates_list)

        # Add the numbers with random coordinates
        for i in range(self.n ** 2 - 1):
            self.board_numbers[coordinates_list[i]] = i + 1
        self.empty_slot: tuple(int, int) = coordinates_list[self.n ** 2 - 1]
        self.board_numbers[self.empty_slot] = 0

    def __str__(self) -> str:
        # TODO: find a better way to visualize this
        res: list[str] = [" "]
        for j in range(self.n):
            for i in range(self.n):
                if self.empty_slot != (i, j):
                    res.append(" " + str(self.board_numbers[(i, j)]) + " ")
                else:
                    res.append(" * ")
            res.append(" \n ")
        taquin_str: str = "".join(res)
        return taquin_str

    def __hash__(self) -> int:
        taquin_hash: int = 0
        ten_multiple: int = 1
        for j in range(self.n):
            for i in range(self.n):
                taquin_hash = taquin_hash + self.board_numbers[(i, j)] * ten_multiple
                ten_multiple = ten_multiple * 10
        return taquin_hash

    def __eq__(self, other: Self) -> bool:
        if isinstance(other, self.__class__):
            return hash(other) == hash(self)
        else:
            return False

    def __ne__(self, other: Self) -> bool:
        return not self.__eq__(other)

    def init_state(self) -> Self:
        print("Use '*' for the empty slot")

        for j in range(self.n):
            print("Insert the ", self.n, "digits of line ", j + 1, ":")
            str_values: list[str] = input().split(" ")
            for i in range(self.n):
                if str_values[i] == "*":
                    self.empty_slot = (i, j)
                    self.board_numbers[(i, j)] = 0
                else:
                    self.board_numbers[(i, j)] = int(str_values[i]) % 9

        if len(self.board_numbers.values()) != len(set(self.board_numbers.values())):
            self.init_state()

    def final_state(self) -> bool:
        final_state: int = 0
        for i in range(1, self.n ** 2 + 1):
            final_state *= 10
            final_state += self.n ** 2 - i
        print(final_state)
        return hash(self) == final_state

    def move_piece(self, new_empty_slot) -> Self:
        new_taquin: Self = deepcopy(self)
        new_taquin.depth = new_taquin.depth + 1
        new_taquin.board_numbers[new_taquin.empty_slot] = new_taquin.board_numbers[new_empty_slot]
        new_taquin.board_numbers[new_empty_slot] = 0
        new_taquin.empty_slot = new_empty_slot
        return new_taquin

    def can_move_left(self) -> Self:
        return self.empty_slot[0] < self.n - 1

    def move_left(self) -> Self:
        return self.move_piece((self.empty_slot[0] + 1, self.empty_slot[1]))

    def can_move_right(self) -> Self:
        return self.empty_slot[0] > 0

    def move_right(self) -> Self:
        return self.move_piece((self.empty_slot[0] - 1, self.empty_slot[1]))

    def can_move_up(self) -> Self:
        return self.empty_slot[1] < self.n - 1

    def move_up(self) -> Self:
        return self.move_piece((self.empty_slot[0], self.empty_slot[1] + 1))

    def can_move_down(self) -> Self:
        return self.empty_slot[1] > 0

    def move_down(self) -> Self:
        return self.move_piece((self.empty_slot[0], self.empty_slot[1] - 1))
