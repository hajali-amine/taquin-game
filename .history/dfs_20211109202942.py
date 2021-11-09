from taquin import Taquin

node = Taquin()
taq = node
opened_nodes = []
closed_nodes = set()
j = 0
while not taq.final_state():
    if str(taq) not in closed_nodes:
        print(taq)
        j = j + 1

        if not taq.cant_go_down():
            down_node = taq.go_down()
            opened_nodes.insert(0, down_node)

        if not taq.cant_go_right():
            right_node = taq.go_right()
            opened_nodes.insert(0, right_node)

        if not taq.cant_go_up():
            up_node = taq.go_up()
            opened_nodes.insert(0, up_node)

        if not taq.cant_go_left():
            left_node = taq.go_left()
            opened_nodes.insert(0, left_node)

        closed_nodes.add(str(taq))
        taq = opened_nodes.pop(0)

    else:
        taq = opened_nodes.pop(0)

print(j)
print(taq)
