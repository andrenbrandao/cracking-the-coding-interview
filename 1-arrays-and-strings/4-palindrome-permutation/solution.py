"""
Problem:

1.4 Palindrome Permutation: Given a texting, write a function to check if it is a permutation of a palin­
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)

Hints: #106, #121, #134, #136

--
Questions:

- Do we ignore case sensitive letters?
A: I think we should convert to lowercase.

- Should spaces be ignored?
A: I would remove all of them

- Is an empty texting a valid palindrome?
A: Yes

--

Algorithm:

Examples:
'': True
'a': True
'ab': False
'bb': True
'bba': True
'Tact Coa': True
'aaabbb' = 'ababab': False

We can have only one letter with an odd count. So, we can check for it and
if we find more than one, we can return False.

"""

from collections import Counter


def palindrome_permutation(text):
    if text == "":
        return True

    text = text.lower().replace(" ", "")

    letter_count = Counter(text)

    odd_count_letters = 0
    for key in letter_count:
        if letter_count[key] % 2 != 0:
            odd_count_letters += 1

            if odd_count_letters > 1:
                return False

    return True


def test(text, expected_answer):
    answer = palindrome_permutation(text)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is wrong. Expected answer is {expected_answer}"
        )


if __name__ == "__main__":
    test("", True)
    test("a", True)
    test("ab", False)
    test("bb", True)
    test("bba", True)
    test("Tact Coa", True)
    test("aaabbb", False)
    print("All tests passed!")
