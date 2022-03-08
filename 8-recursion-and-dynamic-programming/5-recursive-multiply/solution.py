"""
Problem:

8.5 Recursive Multiply: Write a recursive function to multiply two positive
integers without using the * operator.
You can use addition, subtraction, and bit shifting, but you should minimize
the number of those operations.

Hints: #166, #203, #227, #234, #246, #280
--
Questions and Notes:

- Is the goal to minimize the number of operations?
Yes
- Do I have to choose between one of these operations, or should I use
them when needed? For example: can I choose my function to only use addition?
- Are the numbers always greater than zero?

--
Algorithm:

1) Multiplication by an even number
A multiplication by an even number e.g 4 can be made by bit shifting to the left.
It also can be made by summing the number 4 times.
3 * 4 -> 3 + 3 + 3 + 3 or 4 + 4 + 4

2) Multiplication by an odd number
3 * 5 -> 5 + 5 + 5 or 3 + 3 + 3 + 3 + 3.

Both work in the same way if we use addition.
Let's say we are summing A + B and A > B.
Since we want to minimize the number of those operations, we would have
to take A and sum it B times.

Base case:
A = 0 or B = 0: return 0
A = 1: return B
B = 1: return A

Recursive Step:
- Take max(A, B) and recursively sum it with the smallest of them subtracted by 1.

P(max(A,B), min(A, B)) = max(A,B) + P(max(A,B), min(A, B) - 1)

Time Complexity: O(min(A, B))
Space Complexity: O(min(A, B))


-- Dry Run
rec(3, 5)
5 + rec(5, 2)
5 + 5 + rec(5, 1)
5 + 5 + 5
15

-- How to optimize it? --
The book presents a different solution with bit shifting and presents
at the end a Time Complexity of O(logS) being S the smaller of the two numbers.

Reference: https://www.youtube.com/watch?v=b0_S0X1JwGk&ab_channel=EasyTheory

TODO: Understand the explanation.
"""


def recursively_multiply(a, b):
    if a == 0 or b == 0:
        return 0

    if a == 1:
        return b

    if b == 1:
        return a

    return max(a, b) + recursively_multiply(max(a, b), min(a, b) - 1)


def test(a, b, expected_answer):
    answer = recursively_multiply(a, b)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    test(3, 4, 12)
    test(1, 5, 5)
    print("All tests passed!")
