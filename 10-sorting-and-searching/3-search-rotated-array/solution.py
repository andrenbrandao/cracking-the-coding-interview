"""
Problem:

10.3 Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.

EXAMPLE
Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)

Hints:#298, #310

--
Algorithm:

The naive approach would be to just iterate over the array. Time Complexity: O(n)

But,since the array is rotated, we could probably do some time of Binary Search to decrease
this time complexity to O(logn).

How do it do this?

 l               m                      r
{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}

 l                   m                   r
{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}

We have the case when left side is increasing and right side shifts.
The opposite also happens.

So, we have to check if left <= mid. If it is, the left side is increasing.
We can then compare if the target is between left and mid and keep the binary
search in this range.

Otherwise, look at the right side and keep checking this comparison between
the left and mid pointers.

Time Complexity: O(logn)
Space Complexity: O(1)
"""


def search_in_rotated_array(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if target == arr[mid]:
            return mid

        elif arr[left] <= arr[mid]:
            if target >= arr[left] and target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > arr[mid] and target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def test(arr, number, expected_answer):
    answer = search_in_rotated_array(arr, number)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(
        [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14],
        5,
        8,
    )
    test([5], 5, 0)
    test([15, 17, 5, 6], 5, 2)
    test([2, 2, 2, 3, 4, 2], 4, 4)
    test([5, 1, 3], 5, 0)
    print("All tests passed!")
