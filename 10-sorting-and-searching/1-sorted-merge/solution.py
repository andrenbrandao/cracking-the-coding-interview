"""
Problem:

10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.

Hints: #332

--

Questions:

- Can I assume both arrays always have elements in them?

--

Algorithm:

A = [1,4,5,7,8,-,-,-,-]
B = [0,3,4,6]

Result = [0,1,3,4,4,5,6,7,8]


-- Using additional memory --

We want to compare each element of A and B and take the smallest one first.
Add it to a new array of the same size of A.
At the end, copy the elements back to A.

Being n the number of elements in array A and m the size of array B:
Time Complexity: O(n + m)
Space Complexity: O(n + m)

-- In-place --

Shift all elements of A to the end of the array.

             i       j
Shifted A = [-,-,-,-,1,4,5,7,8]
     k
B = [0,3,4,6]

Have two pointers at the beginning of A and one at the first valid element.
Compare B and A elements, storing them in the beginning of A.

Time Complexity: O(n + m)
Space Complexity: O(1)

Although, being O(n+m) in time complexity, this algorithm has to shift all
elements of A to the right. So, it is Theta(2n + m). Can we make it better?

-- Optimizing it --

We could move the pointers to the last elements of each array and
compare them, moving the largest number to the end of the array.

This saves the time of shifting all elements of A to the right.

PS: The book's solution assumes we are given the positions of the last element in A and B.
So, it does not have to iterate over the array to count the elements.
If we do not know these positions, we still have to go through all the elements
of A to know where to position our pointers.

"""


def sorted_merge(arr1, arr2):
    n_elements = count_elements(arr1)
    shift_elements_right(arr1, n_elements)

    i = 0
    j = len(arr1) - n_elements
    k = 0

    while k < len(arr2) and j < len(arr1):
        if arr2[k] < arr1[j]:
            arr1[i] = arr2[k]
            k += 1
        else:
            arr1[i] = arr1[j]
            j += 1
        i += 1

    while k < len(arr2):
        arr1[i] = arr2[k]
        i += 1
        k += 1

    return arr1


def count_elements(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] is not None:
            count += 1

    return count


def shift_elements_right(arr, n_elements):
    n = len(arr)

    for i in range(n_elements):
        arr[n - 1 - i], arr[n_elements - 1 - i] = (
            arr[n_elements - 1 - i],
            arr[n - 1 - i],
        )


def test(arr1, arr2, expected_answer):
    answer = sorted_merge(arr1, arr2)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(
        [1, None],
        [0],
        [0, 1],
    )
    test(
        [1, 4, 5, 7, 8, None, None, None, None],
        [0, 3, 4, 6],
        [0, 1, 3, 4, 4, 5, 6, 7, 8],
    )
    test(
        [1, 4, 5, 7, 8, None, None, None, None],
        [0, 0, 0, 0],
        [0, 0, 0, 0, 1, 4, 5, 7, 8],
    )
    test(
        [1, 4, 5, 7, 8, None, None, None, None],
        [9, 9, 10, 10],
        [1, 4, 5, 7, 8, 9, 9, 10, 10],
    )
    print("All tests passed!")
