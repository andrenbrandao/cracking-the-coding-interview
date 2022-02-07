"""
Problem:

2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

Hints:#8, #25, #41, #67, #126

--

Questions:


--

Algorithm:

5 -> 2 -> 3 -> 0

k = 1

In the example above, we are asking for the 2nd to last element. It would be 3.
k = 0 would return the last element.

-- Naive --

We do not know how long the list is, so we could find this element by first
iterating over the list and counting the number of elements.

Then, iterate over the list and look for the element at position n-k-1,
considering the first position at index 0.

Time Complexity: O(n)

------

Can we do it better by just one go?

     i         j
5 -> 2 -> 3 -> 0

What if we always use two pointers, keeping them at a distance k.
When the second pointer reaches the end, we have the first pointer at
a k distance from the end.

Check if current.next is None. If it is, return the node at pointer 'i'.

Start both pointers at the head. Start moving j and when they have a distance
of k, we can start moving i.
"""

from os import lstat


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


def create_linked_list(elements):
    dummy = Node(-1)

    current = dummy
    for val in elements:
        node = Node(val)
        current.next = node
        current = current.next

    return dummy.next


def kth_to_last_naive(lst, k):
    n = 0
    current = lst
    while current:
        n += 1
        current = current.next

    current = lst

    while current:
        n -= 1
        if n == k:
            return current

        current = current.next

    return Node(None)


def kth_to_last(lst, k):
    dummy = Node(None)
    dummy.next = lst
    current_i = dummy
    current_j = dummy

    distance = 0

    while current_j.next:
        current_j = current_j.next
        if distance == k:
            current_i = current_i.next
        else:
            distance += 1

    return current_i


def test(elements, k, expected_answer):
    linked_list = create_linked_list(elements)
    answer = kth_to_last(linked_list, k).value

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test([5, 2, 3, 4, 0], 2, 3)
    test([5, 2, 3, 4, 0], 1, 4)
    test([5, 2, 3, 4, 0], 4, 5)
    test([5, 2, 3, 4, 0], 0, 0)
    test([5, 2, 1], 3, None)
    print("All tests passed!")
