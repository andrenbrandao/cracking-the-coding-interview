"""
Problem:

4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

Hints: #107, #123, #135

--
Questions

- Should the linked list represent the nodes in the same order they are seen
in the tree? For example, see the example below.

--
Algorithm:

     4        depth: 0
   /   \
  2      6    depth: 1
 / \    / \
1   3  5   7  depth: 2

So, the result would be:

4
2 -> 6
1 -> 3 -> 5 -> 7

That is, we would have an array of linked lists.

- Do a BFS going through each node
- Add each node with the depth to the queue
- After popping the depth and node, check if len(result_arr) > depth
- If yes, we can add it to a linked list in the corresponding position
- If not, we append the node to the result

If we add the nodes to the linked list by iterating over all the elements in the linked list,
the time it would take to add a node to deeper levels would increase over time.
So, it is better to create a LinkedList Class that will add elements to the end.
"""

from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class LinkedListNode:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None) -> None:
        self.head = LinkedListNode(node)
        self.tail = self.head
        self.size = 0

    def add(self, node):
        if self.head is None:
            self.head = LinkedListNode(node)
            self.tail = self.head
        else:
            self.tail.next = LinkedListNode(node)
            self.tail = self.tail.next
        self.size += 1

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next


def list_of_depths(node):
    if not node:
        return []

    queue = deque([])
    result = []

    queue.append((node, 0))
    while queue:
        current, depth = queue.popleft()
        add_to_linked_list(current, result, depth)

        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))

    return result


def add_to_linked_list(node, linked_list_array, pos):
    if len(linked_list_array) > pos:
        current = linked_list_array[pos]
        current.add(node)
    else:
        linked_list_array.append(LinkedList(node))


def get_array_of_values(linked_list_array):
    result = []

    for linked_list in linked_list_array:
        values = []
        for linked_list_node in linked_list:
            values.append(linked_list_node.data.value)

        result.append(values)
    return result


def test(node, expected_answer):
    array_of_linked_list = list_of_depths(node)
    answer = get_array_of_values(array_of_linked_list)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    tree = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))
    )
    test(tree, [[4], [2, 6], [1, 3, 5, 7]])
    test(TreeNode(2), [[2]])
    test(None, [])
    print("All tests passed!")
