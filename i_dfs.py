from taquin import Taquin
from copy import copy, deepcopy


node = Taquin()
taq = deepcopy(node)
opened_nodes = []
closed_nodes = set()
limit = 0
j = 0
while not taq.final_state():
    if taq not in closed_nodes:
        print(taq)
        j = j + 1

        if not taq.can_go_down() and taq.depth < limit:
            down_node = taq.go_down()
            opened_nodes.insert(0, down_node)

        if not taq.can_go_right() and taq.depth < limit:
            right_node = taq.go_right()
            opened_nodes.insert(0, right_node)

        if not taq.can_go_up() and taq.depth < limit:
            up_node = taq.go_up()
            opened_nodes.insert(0, up_node)

        if not taq.can_go_left() and taq.depth < limit:
            left_node = taq.go_left()
            opened_nodes.insert(0, left_node)

        closed_nodes.add(taq)
        if len(opened_nodes) != 0:
            taq = opened_nodes.pop(0)
        else:
            limit = limit + 1
            closed_nodes.clear()
            taq = deepcopy(node)

    else:
        taq = opened_nodes.pop(0)
        closed_nodes.clear()
        taq = deepcopy(node)


print(j)
print(taq)
