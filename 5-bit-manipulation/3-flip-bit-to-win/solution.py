"""
Problem:

5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1s you could create.

EXAMPLE
Input: 1775 (or: 11011101111)
Output: 8

Hints: #159, #226, #314, #352

---
Questions:

- Are the integers 32bit or 64bit?
- Are they non-negative or can they be also negative?

A -1 would basically iterate indefinitely when shifting the bits, because it will never be zero.
When shifting a positive number, the bits to the left are replaced with zeroes.
Negative numbers have them replaced with 1s. So a negative number will always contain 1s.

---

Algorithm:

We can have two sequences, one to the left of a zero and one to the right.
Let's call them previousSequence and currentSequence.

When starting to read the number, our previousSequence has length 0.
Read the digits and when we reach a 0:
1. If the digit after the zero is a 1, we can remember the count until now
as a previousSequence.
2. If the digit after the zero is another zero, we have to start a new sequence,
so previousSequence is zero. Also, merge previousSequence with currentSequence.

previous        current
111        0     111     01

                previous    current
111        0     111     0   1        00

                                         current
111        0     111     0   1        00  1

I had to look the solution up to understand.
"""


def flip_bit_to_win(number):
    max_length = 0
    previous_length = 0
    current_length = 0

    while number != 0:
        if number & 1 == 1:
            current_length += 1

        elif number & 1 == 0:
            if number & 2 == 0:
                previous_length = 0
            else:
                previous_length = current_length
            current_length = 0

        max_length = max(previous_length + current_length, max_length)

        number = number >> 1
    return max_length + 1


def test(number, expected_answer):
    answer = flip_bit_to_win(number)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(1775, 8)
    test(3703, 7)
    test(3959, 8)
    test(0, 1)
    test(511, 10)
    print("All tests passed!")
