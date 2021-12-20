"""
Problem:

4.1 Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""

"""
Questions:

- Are the inputs always going to be valid nodes? Or should we consider inputs
such as None?
- Or, are we receiving an adjacency list as our graph?
- Can there be any cycles?
- What if source and destination are the same node?

--
Algorithm:

Let's consider we receive two valid nodes and that they have a list of neighbors.

We could use DFS to look through all nodes, marking them as visited. If we find
the second node, we know there is a route.

This can also be solved by using BFS, specially if we want to find the shortest
path. I believe this would be the better approach also because it does not use
recursion and we can prevent a stack overflow from happening.

"""

from collections import deque


class Node:
    def __init__(self):
        self.visited = False
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)


def has_path_between_nodes(source, dest):
    if source == dest:
        return True

    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        node = queue.popleft()
        node.visited = True

        for neighbor in node.neighbors:
            if neighbor == dest:
                return True
            if not neighbor.visited:
                queue.append(neighbor)

    return False


def test(source, dest, expected_answer):
    answer = has_path_between_nodes(source, dest)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


# Lets consider nodes from 0 to n-1
def create_graph_from_adjacency_list(adj_list, n):
    nodes = [Node() for _ in range(n)]
    for node1, node2 in adj_list:
        nodes[node1].add_neighbor(nodes[node2])

    return nodes


if __name__ == "__main__":
    # Simple graph
    nodes = create_graph_from_adjacency_list([[0, 1], [0, 2]], 3)
    test(nodes[0], nodes[2], True)
    test(nodes[2], nodes[1], False)

    # Different subgraphs
    nodes = create_graph_from_adjacency_list([[0, 1], [1, 2], [2, 3], [4, 5]], 6)
    test(nodes[0], nodes[3], True)
    test(nodes[0], nodes[5], False)

    # With cycles
    nodes = create_graph_from_adjacency_list(
        [[0, 1], [1, 2], [2, 1], [2, 3], [4, 5]], 6
    )
    test(nodes[0], nodes[3], True)
    test(nodes[0], nodes[5], False)

    # The same node
    nodes = create_graph_from_adjacency_list([[0, 1], [0, 2]], 3)
    test(nodes[0], nodes[0], True)

    print("All tests passed!")
