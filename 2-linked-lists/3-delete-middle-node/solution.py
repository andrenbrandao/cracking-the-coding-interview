"""
Problem:

2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

EXAMPLE

Input: the node c from the linked list a->b->c->d->e->f

Result: nothing is returned, but the new linked list looks like a->b->d->e- >f

Hints: #72

--

Questions:

- Can I be sure the input will always be a node from the middle?
--

Algorithm:

If we only have access to the middle node, there is no way we can iterate
over the list to remove the node.

The solution is then to copy the value from the next node and remove it.

Time Complexity: O(1)
Space Complexity: O(1)

Considerations:

- If the node is the last node we will not be able to remove it.
"""


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


def delete_middle_node(node):
    if not node or not node.next:
        raise Exception("Could not remove node")

    node.value = node.next.value
    node.next = node.next.next


def create_linked_list(elements):
    dummy = Node(-1)

    current = dummy
    for val in elements:
        node = Node(val)
        current.next = node
        current = current.next

    return dummy.next


def get_node(lst, pos):
    current = lst
    count = 0

    while current:
        if count == pos:
            return current

        current = current.next
        count += 1


def linked_list_to_array(lst):
    result = []

    current = lst
    while current:
        result.append(current.value)
        current = current.next

    return result


def test(elements, node_pos, expected_answer):
    linked_list = create_linked_list(elements)
    middle_node = get_node(linked_list, node_pos)
    delete_middle_node(middle_node)
    answer = linked_list_to_array(linked_list)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


def test_raises_exception(elements, node_pos):
    linked_list = create_linked_list(elements)
    middle_node = get_node(linked_list, node_pos)

    try:
        delete_middle_node(middle_node)
    except Exception:
        return True

    raise Exception("Test did not raise exception")


if __name__ == "__main__":
    test([5, 2, 3, 4, 0], 2, [5, 2, 4, 0])
    test([5, 2, 3, 4, 0], 1, [5, 3, 4, 0])
    test([5, 2, 3, 4, 0], 0, [2, 3, 4, 0])
    test_raises_exception([5, 2, 3], 2)
    print("All tests passed!")
