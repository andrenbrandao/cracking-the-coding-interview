"""
Problem:

4.2 Minimal Tree: Given a sorted (increasing order) array with
unique integer elements, write an algorithm to create a binary search tree with minimal height.

Hints: #19, #73, #116


--

Algorithm:

Take the middle element and use it as the root. Then, we will have elements to the
left and to the right. The middle element of the subarray to the left should be
the left child. The same happens to the right child with the right subarray.

We can do this recursively.

Time Complexity: O(n)
Space Complexity: O(logn) considering this will be the tree height

"""

from collections import deque
from re import A


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def minimal_tree(arr) -> Node:
    def create_tree(left, right, arr):
        if left > right:
            return None
        mid = (left + right) // 2

        root = Node(arr[mid])
        root.left = create_tree(left, mid - 1, arr)
        root.right = create_tree(mid + 1, right, arr)

        return root

    return create_tree(0, len(arr) - 1, arr)


def bfs(node):
    if not node:
        return []

    queue = deque([])
    queue.append(node)

    result = []
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


def test(answer, expected_answer):
    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


"""

      4
    /   \
   2     6
  / \   / \
 1  3  5   7

"""
if __name__ == "__main__":
    tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    test(bfs(tree), [4, 2, 6, 1, 3, 5, 7])
    test(bfs(minimal_tree([1, 2, 3, 4, 5, 6, 7])), bfs(tree))
    test(bfs(minimal_tree([1])), [1])
    test(bfs(minimal_tree([1, 2])), [1, 2])
    test(bfs(minimal_tree([])), [])
    test(bfs(minimal_tree([1, 2, 3, 4, 5, 6])), [3, 1, 5, 2, 4, 6])
    print("All tests passed!")
