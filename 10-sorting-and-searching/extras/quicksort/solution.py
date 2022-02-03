"""

[5,2,4,3,1]
     ^
     pivot

Choose a pivot and swap it with the element in the first position.

   j
   i
[4,2,5,3,1]

Have two pointers 'i' and 'j' on the second position.
- i: indicates all elements less than or equal to the pivot
- j: indicates all elements greater than the pivot

So, all elements before i are less than or equal.

   j
 i
[4,2,5,3,1] - a[j] is less than pivot, increment i and swap a[j] and a[i]. Increment j.

     j
   i
[4,2,5,3,1] - a[j] is greater than pivot, increment j.

       j
   i
[4,2,5,3,1] - a[j] is less than pivot, increment i and swap a[j] and a[i]. Increment j.

         j
     i
[4,2,3,5,1] - a[j] is less than pivot, increment i and swap a[j] and a[i]. Increment j.

       i j
[4,2,3,1,5] - now swap pivot and a[i]

[1,2,3,4,5] - luckily it is already sorted, but we might have needed to
keep doing this with the left and right side of the pivot.

Notice that the pivot is already in its place. So we can keep doing it
recursively from 0 to pivot - 1 and pivot + 1 to the end.
"""


def quicksort(arr):
    def sort(arr, left, right):
        if left >= right:
            return

        mid = partition(arr, left, right)
        sort(arr, left, mid - 1)
        sort(arr, mid + 1, right)

    def partition(arr, left, right):
        mid = (left + right) // 2
        pivot = left
        swap(arr, mid, pivot)

        i = left
        j = i + 1

        while j <= right:
            if arr[j] <= arr[pivot]:
                i += 1
                swap(arr, i, j)
                j += 1
            else:
                j += 1

        new_pivot_pos = i
        swap(arr, pivot, new_pivot_pos)
        return new_pivot_pos

    def swap(arr, pos1, pos2):
        arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

    sort(arr, 0, len(arr) - 1)
    return arr


def test(input_data, expected_answer):
    answer = quicksort(input_data)

    if answer != expected_answer:
        raise Exception(
            f"Wrong answer {answer}. Expected answer was {expected_answer}."
        )


if __name__ == "__main__":
    test([5, 2, 4, 3, 1], [1, 2, 3, 4, 5])
    print("All tests passed!")
