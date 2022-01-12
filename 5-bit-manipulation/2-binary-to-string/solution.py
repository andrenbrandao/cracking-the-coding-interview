"""
Problem:

5.2 Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print "ERROR.'

Hints: #143, #167, #173, #269, #297

--
Algorithm:

Since we know it is a number between 0 and 1, we can consider the first part of the binary
number as 0.

To get the mantissa and convert to binary, first notice that 0.9999 would be equal
to 2^-1 + 2^-2 + 2^-2.... which is 0.5 + 0.25 + 0.125 ...

For an integer, we have to divide by 2 and use the remainder as the least significant bit.
Keep doing it by dividing the quotient and getting all the bits until the quotient is 0.

The same way we have to keep dividing an integer by 2 to get the binary representation,
we have to do the same with the mantissa, but by multiplying the numbers by 2.

0.25 * 2 = 0.50 (take 0)
0.50 * 2 = 1.00 (take 1)
(01)₂

0.75 * 2 = 1.50 (take 1)
0.50 * 2 = 1.00 (take 1)
(11)₂

Since we can only have at most 32 characters, we can only have 30 characters
for the mantissa. So, keep doing this multiplication until we find a 1.00. If
we reach over 30 loops, return ERROR.

"""


def bin_to_str(number):
    result = []

    while number != 1.0:
        number = number * 2.0
        digit = int(number)
        result.append(str(digit))

        if len(result) > 32:
            return "ERROR"

        if number > 1.0:
            number -= 1.0

    mantissa = "".join(result)
    return f"0.{mantissa}"


def test(number, expected_answer):
    answer = bin_to_str(number)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test(0.25, "0.01")
    test(0.75, "0.11")
    test(0.33333, "ERROR")
    test(0.2, "ERROR")
    test(0.5, "0.1")

    print("All tests passed!")
