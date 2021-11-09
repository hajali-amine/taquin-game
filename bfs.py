from taquin import Taquin

taq = Taquin()
opened_nodes = [taq]
closed_nodes = set()
i = 0
j = 0
while not opened_nodes[i].final_state():
    if str(opened_nodes[i]) not in closed_nodes:
        print(opened_nodes[i])
        j = j + 1

        if not opened_nodes[i].cant_go_down():
            down_node = opened_nodes[i].go_down()
            opened_nodes.append(down_node)

        if not opened_nodes[i].cant_go_right():
            right_node = opened_nodes[i].go_right()
            opened_nodes.append(right_node)

        if not opened_nodes[i].cant_go_up():
            up_node = opened_nodes[i].go_up()
            opened_nodes.append(up_node)

        if not opened_nodes[i].cant_go_left():
            left_node = opened_nodes[i].go_left()
            opened_nodes.append(left_node)

        closed_nodes.add(str(opened_nodes[i]))

    i = i + 1

print(j)
print(opened_nodes[i])
