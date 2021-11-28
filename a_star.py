from taquin import Taquin


class AStarHeuristics:
    @staticmethod
    def h1(taq):
        # returns number of misplaced numbers
        hash_str = str(hash(taq))[:-1]
        print(hash_str)
        length = len(hash_str)
        return 8 - length + sum(hash_str[i] != "87654321"[8 - length:][i] for i in range(length))

    @staticmethod
    def h2(taq):
        # returns the sum of number of left steps for each number
        right_places = {
            1: (1, 0),
            2: (2, 0),
            3: (0, 1),
            4: (1, 1),
            5: (2, 1),
            6: (0, 2),
            7: (1, 2),
            8: (2, 2)
        }

        result = 0
        for coordinates, value in taq.board_numbers.items():
            if value != 0:
                result = result + abs(right_places[value][0] - coordinates[0]) + abs(
                    right_places[value][1] - coordinates[1])
        return result


# taq = Taquin()
# taq.init_state()
# print(AStarHeuristics.h1(taq))
# print(AStarHeuristics.h2(taq))
