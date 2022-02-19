"""
Problem:

2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Hints: #3, #24

--
Questions:

- So we have to return a new LinkedList where all elements less than x will be
in one side and elements greater than or equal to x will be after them?
Yes
- Can x be null?
No, it will be an integer. But the number may not be in the linked list.
- Are we dealing with only integers?
Yes
- Can the linkedlist be empty?
Yes
- Is the linkedlist singly or doubly linked?
Let's consider it as singly linked.

--
Algorithm:

We can create two linked lists and join them.

                               i
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]

left_list: 3, 2, 1
right_list: 5, 8, 5, 10

Iterate over the linked list.
- If the element is less than x, add it to the left_list.
- Else, add it to the right list.
- Join the lists

joined_list: 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10

Time Complexity: O(n)
Space Complexity: O(n) because we create a new list


-- Running the code:
                               i
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1

left -> 3 -> 2 -> 1 -> None
right -> 5 -> 8 -> 5 -> 10 -> None
"""


class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


def partition(node, target):
    if node is None:
        return None

    current = node
    left_dummy = Node(-1)
    right_dummy = Node(-1)

    left_current = left_dummy
    right_current = right_dummy
    while current is not None:
        if current.value < target:
            left_current.next = current
            left_current = left_current.next
        else:
            right_current.next = current
            right_current = right_current.next

        current = current.next

    right_current.next = None  # So that we don't endup pointing back to another node
    left_current.next = right_dummy.next  # Join the lists

    return left_dummy.next


def test(linked_list, target, expected_answer):
    partitioned_list = partition(linked_list, target)
    answer = [] if partitioned_list is not None else None
    current = partitioned_list

    while current is not None:
        answer.append(current.value)
        current = current.next

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    test(None, 5, None)
    test(Node(3, Node(5, Node(1))), 5, [3, 1, 5])
    test(
        Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1))))))),
        5,
        [3, 2, 1, 5, 8, 5, 10],
    )
    print("All tests passed!")
