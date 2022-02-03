"""
Explanation: https://www.youtube.com/watch?v=OKd534EWcdk&ab_channel=CSDojo

[2,5,2,1,3,1,1]

Given an unsorted array, count the numbers of each entry in a different array.

 0 1 2 3 4 5
[0,3,2,1,0,1]

Then, sum cumilatively from left to right.

 0 1 2 3 4 5
[0,3,5,6,6,7]

Shift the elements to the right.

 0 1 2 3 4 5
[0,0,3,5,6,6]

The numbers now represent how many are less than the current number in the array.
Ex: there are 5 entries less than 3.

Go through all the elements in the array and store the number given its position,
in the auxiliary array. Increment the count by 1.

arr:    [2,5,2,1,3,1,1]

         0 1 2 3 4 5
aux:    [0,0,3(+1),5,6,6]

result: [-,-,-,2,-,-,-]

The first element is 2. Increment 3 by 1. The next time we find 2,
we will use the number 4 as its next position.

"""


def countingsort(arr):
    aux = [0] * (max(arr) + 1)
    result = [None] * len(arr)

    count_elements(arr, aux)
    cumulative_sum(aux)
    shift_right(aux)

    for num in arr:
        pos = aux[num]
        result[pos] = num
        aux[num] += 1

    return result


def count_elements(arr, aux):
    for num in arr:
        aux[num] += 1


def cumulative_sum(aux):
    for i in range(1, len(aux)):
        aux[i] += aux[i - 1]


def shift_right(aux):
    for i in reversed(range(1, len(aux))):
        aux[i] = aux[i - 1]

    aux[0] = 0


def test(input_data, expected_answer):
    answer = countingsort(input_data)

    if answer != expected_answer:
        raise Exception(
            f"Wrong answer {answer}. Expected answer was {expected_answer}."
        )


if __name__ == "__main__":
    test([5, 2, 4, 3, 1], [1, 2, 3, 4, 5])
    test([2, 5, 2, 1, 3, 1, 1], [1, 1, 1, 2, 2, 3, 5])
    test([99, 55, 35, 60, 10, 25], [10, 25, 35, 55, 60, 99])
    print("All tests passed!")
