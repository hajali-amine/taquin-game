import random
from copy import copy, deepcopy

from numpy import equal


class Taquin:

    # Instantiating the Taquin with random values
    def __init__(self):
        self.board_numbers = {}
        self.n = 3  # Board's height and width
        self.depth = 0
        coordinates_list = [(i, j) for i in range(self.n) for j in range(self.n)]
        random.shuffle(coordinates_list)

        # Add the numbers with random coordinates
        for i in range(self.n ** 2 - 1):
            self.board_numbers[coordinates_list[i]] = i + 1
        self.empty_slot = coordinates_list[self.n ** 2 - 1]
        self.board_numbers[self.empty_slot] = 0

    def __str__(self):
        # TODO: find a better way to visualize this
        res = " "
        for j in range(self.n):
            for i in range(self.n):
                if self.empty_slot != (i, j):
                    res = res + " " + str(self.board_numbers[(i, j)]) + " "
                else:
                    res = res + " * "
            res = res + " \n "
        return res

    def __hash__(self):
        taquin_hash = 0
        ten_multiple = 1
        for j in range(self.n):
            for i in range(self.n):
                taquin_hash = taquin_hash + self.board_numbers[(i, j)] * ten_multiple
                ten_multiple = ten_multiple * 10
        return taquin_hash

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(other) == hash(self)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def final_state(self):
        return hash(self) == 876543210

    def can_go_left(self):
        return self.empty_slot[0] < self.n - 1

    def go_left(self):
        new_taquin = deepcopy(self)
        new_taquin.depth = new_taquin.depth + 1
        new_empty_slot = (new_taquin.empty_slot[0] + 1, new_taquin.empty_slot[1])
        new_taquin.board_numbers[new_taquin.empty_slot] = new_taquin.board_numbers[new_empty_slot]
        new_taquin.board_numbers[new_empty_slot] = 0
        new_taquin.empty_slot = new_empty_slot
        return new_taquin

    def can_go_right(self):
        return self.empty_slot[0] > 0

    def go_right(self):
        new_taquin = deepcopy(self)
        new_taquin.depth = new_taquin.depth + 1
        new_empty_slot = (new_taquin.empty_slot[0] - 1, new_taquin.empty_slot[1])
        new_taquin.board_numbers[new_taquin.empty_slot] = new_taquin.board_numbers[new_empty_slot]
        new_taquin.board_numbers[new_empty_slot] = 0
        new_taquin.empty_slot = new_empty_slot
        return new_taquin

    def can_go_up(self):
        return self.empty_slot[1] < self.n - 1

    def go_up(self):
        new_taquin = deepcopy(self)
        new_taquin.depth = new_taquin.depth + 1
        new_empty_slot = (new_taquin.empty_slot[0], new_taquin.empty_slot[1] + 1)
        new_taquin.board_numbers[new_taquin.empty_slot] = new_taquin.board_numbers[new_empty_slot]
        new_taquin.board_numbers[new_empty_slot] = 0
        new_taquin.empty_slot = new_empty_slot
        return new_taquin

    def can_go_down(self):
        return self.empty_slot[1] > 0

    def go_down(self):
        new_taquin = deepcopy(self)
        new_taquin.depth = new_taquin.depth + 1
        new_empty_slot = (new_taquin.empty_slot[0], new_taquin.empty_slot[1] - 1)
        new_taquin.board_numbers[new_taquin.empty_slot] = new_taquin.board_numbers[new_empty_slot]
        new_taquin.board_numbers[new_empty_slot] = 0
        new_taquin.empty_slot = new_empty_slot
        return new_taquin
