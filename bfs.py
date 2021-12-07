from taquin import Taquin

if __name__ == '__main__':
    taq = Taquin()
    taq.init_state()
    opened_nodes = []
    closed_nodes = set()

    while not taq.final_state():
        if taq not in closed_nodes:
            print(taq)

            if taq.can_move_down():
                opened_nodes.append(taq.move_down())

            if taq.can_move_right():
                opened_nodes.append(taq.move_right())

            if taq.can_move_up():
                opened_nodes.append(taq.move_up())

            if taq.can_move_left():
                opened_nodes.append(taq.move_left())

            closed_nodes.add(taq)

        if len(opened_nodes) != 0:
            taq = opened_nodes.pop(0)
        else:
            print("no result")
            break

    print("visited nodes = ", len(closed_nodes))
    print(taq)
