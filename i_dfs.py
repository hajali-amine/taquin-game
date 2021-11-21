from taquin import Taquin


def limited_dfs(taquin, limit):
    taq = taquin
    opened_nodes = []
    closed_nodes = set()

    while not taq.final_state():
        if (taq not in closed_nodes) and (taq.depth <= limit):
            print(taq)

            if taq.can_go_down():
                down_node = taq.go_down()
                opened_nodes.append(down_node)

            if taq.can_go_right():
                right_node = taq.go_right()
                opened_nodes.append(right_node)

            if taq.can_go_up():
                up_node = taq.go_up()
                opened_nodes.append(up_node)

            if taq.can_go_left():
                left_node = taq.go_left()
                opened_nodes.append(left_node)

            closed_nodes.add(taq)

        if len(opened_nodes) != 0:
            taq = opened_nodes.pop()
        else:
            print("no result")
            return False
    print(taq)
    print("limit = ", limit)
    return True


taq = Taquin()
limit = 0
while not limited_dfs(taq, limit) and limit < 200000:
    print("------------------------------------- {} -------------------------------------".format(limit))
    limit = limit + 1
