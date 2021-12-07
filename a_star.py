from taquin import Taquin


class AStarHeuristics:
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


t = Taquin()
t.init_state()
choice = int(input("Choose 1 for h1.\nChoose 2 for h2.\n"))
taq = t, AStarHeuristics.chosen_h(choice, t)
opened_nodes = []
closed_nodes = set()

while not taq[0].final_state():
    if taq[0] not in closed_nodes:
        print(taq[0])

        if taq[0].can_move_down():
            down = taq[0].move_down()
            opened_nodes.append((down, down.depth + AStarHeuristics.chosen_h(choice, down)))

        if taq[0].can_move_right():
            right = taq[0].move_right()
            opened_nodes.append((right, right.depth + AStarHeuristics.chosen_h(choice, right)))

        if taq[0].can_move_up():
            up = taq[0].move_up()
            opened_nodes.append((up, up.depth + AStarHeuristics.chosen_h(choice, up)))

        if taq[0].can_move_left():
            left = taq[0].move_left()
            opened_nodes.append((left, left.depth + AStarHeuristics.chosen_h(choice, left)))

        closed_nodes.add(taq[0])

    if len(opened_nodes) != 0:
        taq = min(opened_nodes, key=lambda x: x[1])
        opened_nodes.remove(taq)
    else:
        print("no result")
        break

print("visited nodes = ", len(closed_nodes))
print(taq[0])
