"""
Problem:

5.4 Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.

Hints: #147, #175, #242, #312, #339, #358, #375, #390

--

Questions:

- Are we considering only non-negative numbers? Or should we also consider negative ones?
Let's consider only non-negative

- Are we dealing with 32 or 64 bits?
64 bits


--
Algorithm:

01111...1111: largest number
00000...0001: smallest
00000...0000: zero

Examples:

1: 00000...0001
To get the largest number, we could shift the 1 to the left until we get the largest one.
The smallest is itself, because we cannot shift to the right without removing any ones.

63          0
 010000.00000
We have to shift the one until the second last bit. The last bit would turn the number
into negative.

What are the max and min numbers we can have?

max = 011111.11111
MAX_NUMBER = 2^62+2^61+2^60..+2^0 = 2^63 - 1
MIN_NUMBER = 1

So, if the input is MAX_NUMBER, the answer would be (MAX_NUMBER, MAX_NUMBER)
If the input is MIN_NUMBER, the answer would be (2^62, MIN_NUMBER)

Let's think about another example:
5: 0000...0101
Here, instead of shifting the bits to the right, we actually would need to count
the numbers of ones, and then position them in the beginning. So, our previous
thought was incorrect.

Next option:
- Count the number of 1 bits
- Position them in the least significant bits to the get the minimum value
- Position them in the most significant bits (without the last) to get the max value
- Return [smallest, largest]

Time Complexity: O(n) being n the number of bits


-- How can we position the bits on the most significant bits?
We can use the min_number shifted to the left.

00000..00000
00000..00111 -> min_number
------------
01110..00000 -> max_number

Total: 64 bits

000011
011000
We want to shift total_bits - count_1s - 1.

0000000011
0110000000
total_bits = 10
count_1s = 2
shift = 7

So, shift min_number to the left (64 - count_1s - 1) times.


---
Exercise Statistics

Elapsed Time: 32min

TODO: The book talks about optimal solutions to the problem. Understand it.
"""


def next_number(number):
    count_1s = count_1_bits(number)

    min_number = 0
    count = count_1s
    while count > 0:
        min_number = min_number << 1
        min_number += 1
        count -= 1

    shift_times = 64 - count_1s - 1
    max_number = min_number
    while shift_times > 0:
        max_number = max_number << 1
        shift_times -= 1

    return [min_number, max_number]


def count_1_bits(number):
    count = 0

    while number != 0:
        if number & 1:
            count += 1
        number = number >> 1
    return count


def test(number, expected_answer):
    answer = next_number(number)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(1, [1, 2 ** 62])

    # 0000...111
    # 0111...000
    test(7, [7, 2 ** 62 + 2 ** 61 + 2 ** 60])

    # 0000...101 - 5
    # 0000...011 - min
    # 0110...000 - max
    test(5, [3, 2 ** 62 + 2 ** 61])
    print("All tests passed!")
