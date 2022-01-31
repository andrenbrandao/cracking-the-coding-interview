"""
Problem:

8.3 Magic Index: A magic index in an array A [ 0 ... n -1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.

FOLLOW UP
What if the values are not distinct?

Hints:#170, #204, #240, #286, #340

--

Questions:

- Can the input be an empty array or None?
- Can the integers be negative?

--
Algorithm:

Iterate over each element in the array and check if A[i] is equal to i.
Time Complexity: O(n)

--Can we do better?--

Considering the array is always sorted and the elements are distinct, can we use binary search?

Let's suppose we have an array [1,2,3...]. Notice that on the first position at index 0, we have
the value 1, which is greater and won't be a magic index. Any other number after it will always
be greater than its index.

Therefore, if we find a number that is greater than its index, we can discard all the numbers
after it.

The same is true to if we find a number that is less than its index. We can discard all
numbers before it.

The only tricky problem is that by using binary search we might return one of the magic
indexes, but it may not be the first.


"""


def find_magic_index(arr):
    for i, val in enumerate(arr):
        if val == i:
            return i

    return -1


def find_magic_index_binary_search(arr):
    n = len(arr)

    def bin_search(left, right, arr):
        if left > right:
            return -1

        mid = (right - left) // 2 + left
        if mid == arr[mid]:
            return mid

        elif arr[mid] < mid:
            return bin_search(mid + 1, right, arr)

        else:
            return bin_search(left, mid - 1, arr)

    return bin_search(0, n - 1, arr)


def test(arr, expected_answer):
    answer = find_magic_index_binary_search(arr)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test([0], 0)
    test([-20, -15, -10, 3, 5, 10], 3)
    print("All tests passed!")
