"""
Problem:

8.4 Power Set: Write a method to return all subsets of a set.

Hints: #273, #290, #338, #354, #373

--

Algorithm:

A set of numbers, or elements, means that all the elements are distinct.
A subset is a set that has some elements of this larger set.

set: {1,5,8}
subsets:
{}
{1}
{5}
{8}
{1,5}
{1,8}
{5,8}
{1,5,8}

The order of the elements is not important. The base case is an empty set.

{1,5} can be built with subsets of {1} and {5}
{1,8} can be built with subsets of {1} and {8}
{5,8} can be built with subsets of {5} and {8}
{1,5,8} can be built with subsets of {1,5}, {1,8} and {5, 8}.

start:          {}
    /            |               \
   {1}          {5}             {8}
   / \          / \             /    \
{1,5}{1,8}   {1,5} {5,8}      {1,8}  {5,8}
 /     ..
{1,5,8}...

[]
[1,5,8]
i

Let's start with an empty array. We could add any elements to the right
of the empty array to our new set.

[1],    [5], [8] -> subsets
[5,8]   [8]  [] -> elements left

[1,5] [1,8] [5,8] -> subsets
[8]    []     []  -> elements left

[1,5,8] -> subset

---
i = len(subset)

So, we can use this pointer to check on every new element we can add to our subsets.

Time Complexity: O(n*2^n)
Space: O(n*2^n)
We are generating 2^n subsets that can be at most of size n.

Other solutions:
- https://www.youtube.com/watch?v=REOH22Xwdkk&ab_channel=NeetCode
- https://leetcode.com/problems/subsets/solution/
"""


def power_set(arr):
    subsets = [[]]

    def find_subsets(arr, pos, current_subset):
        if pos >= len(arr):
            return

        for i in range(pos, len(arr)):
            subsets.append(current_subset + [arr[i]])
            find_subsets(arr, i + 1, current_subset + [arr[i]])

    find_subsets(arr, 0, [])
    return subsets


def test(arr, expected_answer):
    answer = power_set(arr)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test([1], [[], [1]])
    test([1, 2], [[], [1], [1, 2], [2]])
    test([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
    print("All tests passed!")
