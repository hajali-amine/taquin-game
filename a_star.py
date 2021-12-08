from taquin import Taquin


class AStarHeuristics:
    opened_nodes = [[]]

    @staticmethod
    def add_to_opened_nodes(taq, f):
        if len(AStarHeuristics.opened_nodes) <= f:
            AStarHeuristics.opened_nodes = [AStarHeuristics.opened_nodes[i] if i < len(AStarHeuristics.opened_nodes) else [] for i in range(f + 1)]
        AStarHeuristics.opened_nodes[f].append(taq)

    @staticmethod
    def get_from_opened_nodes():
        i = 0
        while i < len(AStarHeuristics.opened_nodes) and not AStarHeuristics.opened_nodes[i]:
            i = i + 1
        if i == len(AStarHeuristics.opened_nodes):
            return None
        else:
            return AStarHeuristics.opened_nodes[i].pop(0)

    @staticmethod
    def chosen_h(choice, taq):
        if choice == 1:
            return AStarHeuristics.h1(taq)
        if choice == 2:
            return AStarHeuristics.h2(taq)
        else:
            raise Exception("bro, wrong number")

    @staticmethod
    def h1(taq):
        # returns number of misplaced numbers
        hash_str = str(hash(taq))[:-1]
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


if __name__ == '__main__':
    taq = Taquin()
    taq.init_state()
    choice = int(input("Choose 1 for h1.\nChoose 2 for h2.\n"))
    closed_nodes = set()

    while not taq.final_state():
        if taq not in closed_nodes:
            print(taq)

            if taq.can_move_down():
                down = taq.move_down()
                AStarHeuristics.add_to_opened_nodes(down, down.depth + AStarHeuristics.chosen_h(choice, down))

            if taq.can_move_right():
                right = taq.move_right()
                AStarHeuristics.add_to_opened_nodes(right, right.depth + AStarHeuristics.chosen_h(choice, right))

            if taq.can_move_up():
                up = taq.move_up()
                AStarHeuristics.add_to_opened_nodes(up, up.depth + AStarHeuristics.chosen_h(choice, up))

            if taq.can_move_left():
                left = taq.move_left()
                AStarHeuristics.add_to_opened_nodes(left, left.depth + AStarHeuristics.chosen_h(choice, left))

            closed_nodes.add(taq)

        taq = AStarHeuristics.get_from_opened_nodes()
        if taq is None:
            print("no result")
            break

    print("visited nodes = ", len(closed_nodes))
    if taq is not None:
        print("cost = ", taq.depth)
        print(taq)
