"""

[99, 55, 105, 30, 120]

For radix sort, we want to use counting sort only on the digits, starting from
right to left.

If we used counting sort directly on very big numbers, we would have:
Time Complexity: O(n + k)
Memory: O(n + k)
Being k the range of numbers from 0 to the maximum.

With Radix Sort, we do not have to create an array of size 'k' for the range of
numbers. We can deal with only the digits from 0 to 9.
We are considering here digits 0-9. But, if we sort using a different base,
we can have k with a different range.

Therefore, Radix Sort complexity is the number of digits times the number
of executed Counting Sorts.

Let's consider 'b' as the base used for the numbers and 'd' the max number of digits.

Time Complexity: O(d*(n+b))
Memory: O(n + b)


--- TODO ---
[] Implement it for negative numbers
[] Can we remove the Number class and make the code cleaner?
"""


class Number:
    def __init__(self, value, base=10):
        self.value = value
        self.digit = value % base
        self.base = base

    def save_n_digit(self, n_digit):
        self.digit = self.value // (10 ** n_digit) % self.base

    def __lt__(self, other):
        return self.digit < other.digit

    def __eq__(self, other):
        return self.digit == other.digit


def radixsort(arr):
    max_number_digits = count_digits(max(arr))
    sorted_arr = list(map(Number, arr))

    for i in range(max_number_digits):
        sorted_arr = countingsort(sorted_arr)
        for j in range(len(sorted_arr)):
            sorted_arr[j].save_n_digit(i + 1)

    return [num.value for num in sorted_arr]


def count_digits(number):
    count = 0

    while number != 0:
        number = number // 10
        count += 1
    return count


def countingsort(arr):
    aux = [0] * (max(arr, key=lambda x: x.digit).digit + 1)
    result = [None] * len(arr)

    count_elements(arr, aux)
    cumulative_sum(aux)
    shift_right(aux)

    for num in arr:
        pos = aux[num.digit]
        result[pos] = num
        aux[num.digit] += 1

    return result


def count_elements(arr, aux):
    for num in arr:
        aux[num.digit] += 1


def cumulative_sum(aux):
    for i in range(1, len(aux)):
        aux[i] += aux[i - 1]


def shift_right(aux):
    for i in reversed(range(1, len(aux))):
        aux[i] = aux[i - 1]

    aux[0] = 0


def test(input_data, expected_answer):
    answer = radixsort(input_data)

    if answer != expected_answer:
        raise Exception(
            f"Wrong answer {answer}. Expected answer was {expected_answer}."
        )


if __name__ == "__main__":
    test([5, 2, 4, 3, 1], [1, 2, 3, 4, 5])
    test([2, 5, 2, 1, 3, 1, 1], [1, 1, 1, 2, 2, 3, 5])
    test([99, 55, 35, 60, 10, 25], [10, 25, 35, 55, 60, 99])
    print("All tests passed!")
