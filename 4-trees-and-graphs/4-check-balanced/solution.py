"""
Problem:

4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

Hints: #21, #33, #49, #105, #124

--

Questions:

- Can I assume I will receive the root of the binary tree?
Yes
- Can the input be None?
Yes

Algorithm:

     3
    / \
   2   5
      / \
     4   7

This one is considered balanced. Left height is 1 and Right height is 2 at the root.


     3
    / \
   2   5
      / \
     4   7
          \
           9

This one is unbalanced.

So, we can use DFS to calculate the height of each left and right subtree. If the diff of heights
is > 1, we know it is not balanced.

The only catch is how to return from the DFS as soon as we find it is unbalanced.

Time Complexity: O(n)
Space Complexity: O(n) in worst case because of the call stack

-- Follow up:
Can we optimize it by returning as soon as we find it is false?
"""


from numpy import right_shift


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


# With follow up
def check_balanced(root):
    balanced = True

    def dfs(root):
        nonlocal balanced

        if root is None:
            return 0

        left_height = dfs(root.left)
        # return as soon as we find it is unbalanced
        if left_height == -1:
            return -1

        right_height = dfs(root.right)
        # return as soon as we find it is unbalanced
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            balanced = False
            return -1

        return 1 + max(left_height, right_height)

    dfs(root)
    return balanced


# First solution
def check_balanced_1(root):
    balanced = True

    def dfs(root):
        nonlocal balanced

        if root is None:
            return 0

        left_height = dfs(root.left)
        right_height = dfs(root.right)

        if abs(left_height - right_height) > 1:
            balanced = False

        return 1 + max(left_height, right_height)

    dfs(root)
    return balanced


def test(node, expected_answer):
    answer = check_balanced(node)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    tree = Node(3, Node(2), Node(5, Node(4), Node(7, None, Node(9))))
    test(tree, False)
    tree = Node(3, Node(2), Node(5, Node(4), Node(7)))
    test(tree, True)
    test(None, True)
    test(Node(5), True)
    tree = Node(3, Node(2, Node(1, Node(0))))
    test(tree, False)
    print("All tests passed!")
