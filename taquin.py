import random
from copy import copy, deepcopy


class Taquin:

    def __init__(self):
        self.n = 3  # Board's height and width
        self.depth = 0
        # Instantiating the Taquin with random values
        self.board_numbers = {}
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

    def init_state(self):
        print("Use '*' for the empty slot")

        for j in range(self.n):
            print("Insert the ", self.n, "digits of line ", j + 1, ":")
            str_values = input().split(" ")
            for i in range(self.n):
                if str_values[i] == "*":
                    self.empty_slot = (i, j)
                    self.board_numbers[(i, j)] = 0
                else:
                    self.board_numbers[(i, j)] = int(str_values[i]) % 9

        if len(self.board_numbers.values()) != len(set(self.board_numbers.values())):
            self.init_state()

    def final_state(self):
        return hash(self) == 876543210

    def move_piece(self, new_empty_slot):
        new_taquin = deepcopy(self)
        new_taquin.depth = new_taquin.depth + 1
        new_taquin.board_numbers[new_taquin.empty_slot] = new_taquin.board_numbers[new_empty_slot]
        new_taquin.board_numbers[new_empty_slot] = 0
        new_taquin.empty_slot = new_empty_slot
        return new_taquin

    def can_move_left(self):
        return self.empty_slot[0] < self.n - 1

    def move_left(self):
        return self.move_piece((self.empty_slot[0] + 1, self.empty_slot[1]))

    def can_move_right(self):
        return self.empty_slot[0] > 0

    def move_right(self):
        return self.move_piece((self.empty_slot[0] - 1, self.empty_slot[1]))

    def can_move_up(self):
        return self.empty_slot[1] < self.n - 1

    def move_up(self):
        return self.move_piece((self.empty_slot[0], self.empty_slot[1] + 1))

    def can_move_down(self):
        return self.empty_slot[1] > 0

    def move_down(self):
        return self.move_piece((self.empty_slot[0], self.empty_slot[1] - 1))
