"""
Problem:

2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

Hints: #9, #40

--
Questions:

- Is the linked list singly or doubly linked?
A: Singly.

--

Algorithm:

- Create a Set and every time a node is read, check if the value is already in the set.
- If it is, then we remove the node from the list.
- Else, add it to the set.

To remove the node from the list, we always have to keep a pointer to the last node.

"""


class Node:
    def __init__(self, value, next_node=None):
        self.next = next_node
        self.value = value

    def add_next(self, node):
        self.next = node


def create_linked_list(values):
    if not values:
        return []

    root = Node(values[0])

    node = root
    for val in values[1:]:
        new_node = Node(val)
        node.add_next(new_node)
        node = new_node

    return root


def linked_list_to_array(node):
    result = []

    while node:
        result.append(node.value)
        node = node.next

    return result


def remove_dups(node):
    value_set = set()

    last_node = None
    while node:
        if node.value in value_set:
            last_node.next = node.next
        else:
            value_set.add(node.value)
            last_node = node
        node = node.next


def test(node, expected_answer):
    remove_dups(node)

    answer_as_array = linked_list_to_array(node)

    if answer_as_array != expected_answer:
        raise Exception(
            f"Answer {answer_as_array} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(create_linked_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    test(create_linked_list([1, 2, 3, 4, 3, 5]), [1, 2, 3, 4, 5])
    test(create_linked_list([1, 1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
    test(create_linked_list([1, 1, 1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
    test(create_linked_list([]), [])
    print("All tests passed!")
