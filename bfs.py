from taquin import Taquin

taq = Taquin()
opened_nodes = []
closed_nodes = set()

while not taq.final_state():
    if taq not in closed_nodes:
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
        taq = opened_nodes.pop(0)
    else:
        print("no result")
        break

print(len(closed_nodes))
print(taq)
