import itertools
import random


class Taquin:

    # Instantiating the Taquin with random values
    def __init__(self):
        self.board_numbers = {}
        self.n = 3  # Board's height and width
        coordinates_list = [(i, j) for i in range(self.n) for j in range(self.n)]
        random.shuffle(coordinates_list)

        # Add the numbers with random coordinates
        for i in range(self.n ** 2 - 1):
            self.board_numbers[coordinates_list[i]] = i + 1
        self.empty_slot = coordinates_list[self.n ** 2 - 1]

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

    def go_left(self):
        if self.empty_slot[0] == self.n - 1:
            print("You can't move left monsieur")
        else:
            new_empty_slot = (self.empty_slot[0] + 1, self.empty_slot[1])
            self.board_numbers[self.empty_slot] = self.board_numbers[new_empty_slot]
            self.board_numbers.pop(new_empty_slot)
            self.empty_slot = new_empty_slot

    def go_right(self):
        if self.empty_slot[0] == 0:
            print("You can't move right monsieur")
        else:
            new_empty_slot = (self.empty_slot[0] - 1, self.empty_slot[1])
            self.board_numbers[self.empty_slot] = self.board_numbers[new_empty_slot]
            self.board_numbers.pop(new_empty_slot)
            self.empty_slot = new_empty_slot

    def go_up(self):
        if self.empty_slot[1] == self.n - 1:
            print("You can't move up monsieur")
        else:
            new_empty_slot = (self.empty_slot[0], self.empty_slot[1] + 1)
            self.board_numbers[self.empty_slot] = self.board_numbers[new_empty_slot]
            self.board_numbers.pop(new_empty_slot)
            self.empty_slot = new_empty_slot

    def go_down(self):
        if self.empty_slot[1] == 0:
            print("You can't move down monsieur")
        else:
            new_empty_slot = (self.empty_slot[0], self.empty_slot[1] - 1)
            self.board_numbers[self.empty_slot] = self.board_numbers[new_empty_slot]
            self.board_numbers.pop(new_empty_slot)
            self.empty_slot = new_empty_slot


taquin = Taquin()
print(taquin)
taquin.go_left()
print(taquin)
taquin.go_up()
print(taquin)
taquin.go_down()
print(taquin)
taquin.go_right()
print(taquin)
