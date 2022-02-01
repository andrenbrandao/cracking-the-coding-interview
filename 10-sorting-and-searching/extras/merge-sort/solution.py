"""
            [3,5,2,4,1,3]
                /     \
            [3,5,2]   [4,1,3]
            /   \       /   \
          [3,5]  [2]  [4,1] [3]
          /   \       /   \
         [3]  [5]    [4]  [1]           ---- mergesort until here breaks the arrays
           \  /        \  /
           [3,5] [2]  [1,4]  [3]        ---- here it starts merging them
             \   /      \    /
            [2,3,5]     [1,3,4]
                  \     /
                [1,2,3,3,4,5]

To profile the memory usage, run the commands below, changing
the method `mergesort` by `mergesort_less_memory` in test.py.

$ mprof run 10-sorting-and-searching/extras/merge-sort/test.py 1
$ mprof plot

To change the size of the array, modify the n variable in file gen.py.

-- Memory Comparison --

I have compared the memory usage between the two methods:

- mergesort:             slice_array_memory_usage.png
- mergesort_less_memory: reference_array_memory_usage.png

The first one used up 700MB and the second ~540MB. Which is 22% less memory.
Therefore, slicing the array and making a copy of it uses a lot more memory
than just referencing the positions.

"""


def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_side = mergesort(arr[mid:])
    right_side = mergesort(arr[:mid])
    return merge(left_side, right_side)


def merge(left_arr, right_arr):
    result = []

    i = 0
    j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        result.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        result.append(right_arr[j])
        j += 1

    return result


def mergesort_less_memory(arr):
    helper = [0] * len(arr)

    def _mergesort(arr, left, right, helper):
        if left >= right:
            return

        mid = (left + right) // 2
        _mergesort(arr, left, mid, helper)
        _mergesort(arr, mid + 1, right, helper)
        _merge(arr, left, mid, right, helper)

    def _merge(arr, left, mid, right, helper):
        pos = left
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                helper[pos] = arr[i]
                i += 1
                pos += 1
            else:
                helper[pos] = arr[j]
                j += 1
                pos += 1

        while i <= mid:
            helper[pos] = arr[i]
            i += 1
            pos += 1

        while j <= right:
            helper[pos] = arr[j]
            j += 1
            pos += 1

        pos = left
        for i in range(left, right + 1):
            arr[i] = helper[pos]
            pos += 1

    _mergesort(arr, 0, len(arr) - 1, helper)
    return arr


def test(input_data, expected_answer):
    answer = mergesort_less_memory(input_data)

    if answer != expected_answer:
        raise Exception(
            f"Wrong answer {answer}. Expected answer was {expected_answer}."
        )


if __name__ == "__main__":
    test([5, 2, 4, 3, 1], [1, 2, 3, 4, 5])
    print("All tests passed!")
