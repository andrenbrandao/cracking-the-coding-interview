import random
from solution import Node


def gen(n):
    random.seed(n)

    root = Node(random.randint(1, 100))
    nodes = [root]
    for _ in range(n):
        node = Node(random.randint(1, 100))
        random_node = nodes[random.randint(0, len(nodes) - 1)]
        side = random.choice([0, 1])
        if side == 0:
            random_node.left = node
        else:
            random_node.right = node

        nodes.append(node)

    return root
