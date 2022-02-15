"""
If we add the nodes to the linked list by iterating over all the elements in the linked list,
the time it would take to add a node to deeper levels would increase over time.

     4        depth: 0, elements: 2^0
   /   \
  2      6    depth: 1, elements: 2^1
 / \    / \
1   3  5   7  depth: 2, elements: 2^2

At each depth we have at most 2^depth elements.
How can we know the height of the tree based on the number of elements?

N = 2^0+2^1+2^2...+2^d
The Sum(2^k) from 0 to d = 2^(d+1) - 1 (lookup geometric progression, or this clever proof: https://math.stackexchange.com/questions/1990137/the-idea-behind-the-sum-of-powers-of-2)
So N = 2^(d+1) - 1 => 2^(d+1) = N + 1
=> d+1 = log(N+1) => d = ceil(log(N+1)) - 1

To find the number of elements in a depth, we can do 2^d = 2^(ceil(log(N+1)) - 1)
That means, that every time we add a new element to a linked list, we would be iterating
over this number of elements.
Converting it to Big O Notation:

2^(ceil(log(N+1)) - 1) => O(2^(logN)) => O(N)

So, adding to a Linked List would be O(N).
And, since we have to pass through all the nodes, which is O(N), while adding to the
Linked List, this whole operation would be O(N^2).

That means, that as we grow our tree, the time complexity increases quadratically.
"""

from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class LinkedListNode:
    def __init__(self, node, next=None) -> None:
        self.node = node
        self.next = next


def list_of_depths_non_optimal(node):
    if not node:
        return []

    queue = deque([])
    result = []

    queue.append((node, 0))
    while queue:
        current, depth = queue.popleft()
        add_to_linked_list_non_optimal(current, result, depth)

        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))

    return result


"""
Here, we have to go through all elements of the list to add
the node to the end. Can we do better?

The book has a good solution for it.
"""


def add_to_linked_list_non_optimal(node, linked_list_array, pos):
    if len(linked_list_array) > pos:
        current = linked_list_array[pos]
        while current.next:
            current = current.next
        current.next = LinkedListNode(node)

    else:
        linked_list_array.append(LinkedListNode(node))


def get_array_of_values(linked_list_array):
    result = []

    for linked_list in linked_list_array:
        current = linked_list
        values = []
        while current:
            values.append(current.node.value)
            current = current.next

        result.append(values)
    return result


def test(node, expected_answer):
    array_of_linked_list = list_of_depths_non_optimal(node)
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
