from taquin import Taquin

def limited_dfs(taquin, limit):
    taq = taquin
    opened_nodes = []
    closed_nodes = set()

    while not taq.final_state():
        if (taq not in closed_nodes) and (taq.depth <= limit):
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
            taq = opened_nodes.pop()
        else:
            print("no result")
            return False, len(closed_nodes)

    print(taq)
    print("limit = ", limit)
    return True, len(closed_nodes)


if __name__ == '__main__':
    taq = Taquin()
    taq.init_state()
    limit = 0
    visited_nodes = 0
    last_visited_nodes = 0
    dfs_result = limited_dfs(taq, limit)

    while not dfs_result[0] and last_visited_nodes != dfs_result[1]:
        print("------------------------------------- {} -------------------------------------".format(limit))
        visited_nodes = visited_nodes + dfs_result[1]
        limit = limit + 1
        last_visited_nodes = dfs_result[1]
        dfs_result = limited_dfs(taq, limit)

    print("visited nodes = ", visited_nodes)
