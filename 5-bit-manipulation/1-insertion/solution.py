"""
Problem:

5.1 Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

EXAMPLE
Input: N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100

--
Questions:

- Are the inputs bit numbers using string representations or integers?
- Should the output be an integer or a string representing the bits?

I am going to consider input and output as integers.

--
Algorithm:

    j   i
10000000000

Since we have to fit M inside the j-i space, we could zero all the elements inside
it and do a OR bitwise operation with M shifted to the left.

- Create a mask with zeroes in the window range j-i+1
- Do a bitwise AND with N
- Shift M i times to the left
- Do a OR operation with M
"""


"""Create a mask with zeros in a window from i to j

1111000001111

To do something like above, we have to create a mask with 1s for
the right side and left side and then merge.

Right Side
- Shift 1 i times to the left and subtract 1

Left Side
- Take -1 and shift it j + 1 to the left

"""


def create_mask(i, j):
    right_side = (1 << i) - 1
    left_side = -1 << (j + 1)

    return right_side | left_side


def insert_bits(n, m, i, j):
    window_mask = create_mask(i, j)
    n_cleared = n & window_mask

    shifted_m = m << i
    return n_cleared | shifted_m


def test(n, m, i, j, expected_answer):
    answer = insert_bits(n, m, i, j)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer:0b} is wrong. Expected answer is {expected_answer:0b}"
        )


if __name__ == "__main__":
    test(0b10000000000, 0b10011, 2, 6, 0b10001001100)
    test(0b10001111101, 0b10011, 2, 6, 0b10001001101)

    print("All tests passed!")
