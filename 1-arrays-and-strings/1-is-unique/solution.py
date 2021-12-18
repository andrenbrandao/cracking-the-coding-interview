"""
Problem:

1.1 Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

"""
Questions:

- Are the characters in the string ASCII or Unicode?
- Can the input be None or will it always be a valid string?
- What about spaces? Should we consider them as different characters or should we remove them?

Algorithm:

--Option 1--
We could create a Set of the characters and check if the length is the same as the string.
If it is the same, it has all unique characters.

Time Complexity: O(n)
Space Complexity: O(n)

"""


def is_unique(input_str):
    return len(set(input_str)) == len(input_str)


def test(input_data, expected_answer):
    answer = is_unique(input_data)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test("", True)
    test("a", True)
    test("abc", True)
    test("abbc", False)
    test("abcdefghijklmnopqrstuvwxyz", True)
    print("All tests passed!")
